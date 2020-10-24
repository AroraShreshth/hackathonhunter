from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import send_mail
import uuid
import random
from django.core.mail import send_mail
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit import ImageSpec
from vacc.settings import website_name, EMAIL_HOST_USER
from game.models import Level


def random_no():
    return random.randint(120930, 999999)


class BaseClass(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Institute(BaseClass):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class FieldofStudy(BaseClass):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Skill(BaseClass):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class School(BaseClass):
    name = models.CharField(max_length=300)
    affiliation_no = models.PositiveIntegerField(null=True)
    state = models.CharField(max_length=150, null=True)
    district = models.CharField(max_length=150, null=True)
    region = models.CharField(max_length=150, null=True)
    address = models.TextField(null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True)
    ph_no = models.CharField(max_length=30, null=True)
    off_ph_no = models.CharField(max_length=30, null=True)
    res_ph_no = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    year_found = models.PositiveSmallIntegerField(blank=True, null=True)
    date_opened = models.DateField(null=True)
    principal_name = models.CharField(max_length=150, null=True)
    principal_qual = models.CharField(max_length=150, null=True)
    principal_exp_teach = models.PositiveSmallIntegerField(null=True)
    principal_exp_adm = models.PositiveSmallIntegerField(null=True)
    status = models.CharField(null=True, max_length=100)
    society_name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'{self.name}, {self.district}, {self.region}'


class City(BaseClass):
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.state}'


class Profile(BaseClass):

    # Logical Stuff
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail_is_verified = models.BooleanField(default=False)
    phone_is_verified = models.BooleanField(default=False)
    verification_mail_sent = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    setup = models.BooleanField(default=False)
    # About User
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=5000, null=True, blank=True)

    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 80})
    dob = models.DateField(null=True, blank=True)
    mail_otp = models.PositiveBigIntegerField(
        default=random_no)
    phone_otp = models.PositiveBigIntegerField(
        default=random_no)

    SHIRT_SIZES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X Large'),
        ('XXL', 'XX Large'),
        ('XXXL', 'XXX Large'),
    )
    shirt_size = models.CharField(
        max_length=4, choices=SHIRT_SIZES, blank=True)

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
        ('P', 'Prefer Not To Say'),
        ('N', 'Non Binary,Gender Queer or gender non-confirming')
    )
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)

    level = models.ForeignKey(
        Level, related_name='profile', on_delete=models.SET_NULL, null=True)
    # Education

    no_formal_education = models.BooleanField(default=False)

    completed_school = models.BooleanField(default=False)

    DEGREE_TYPE = (
        ('PhD', 'PhD'),
        ('Associate', 'Associate'),
        ('Masters', 'Masters'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma')
    )

    degree_type = models.CharField(
        max_length=12, choices=DEGREE_TYPE, blank=True)
    institute = models.ForeignKey(
        Institute, related_name='profiles', on_delete=models.PROTECT, null=True, blank=True)
    field_of_study = models.ForeignKey(
        FieldofStudy, related_name='profiles', on_delete=models.PROTECT, null=True, blank=True)
    grad_year = models.DateField(null=True, blank=True)
    LENGTH_COURSE = (
        ('3', '3 year'),
        ('4', '4 year'),
        ('5', '5 year')
    )
    course_length = models.CharField(max_length=1, choices=LENGTH_COURSE)

    # Experience
    skill = models.ManyToManyField(
        Skill, related_name='profiles', blank=True)

    def user_directory_path(self, instance, filename):
        return 'user_{0}/{1}'.format(instance.user.username, filename)

    resume = models.FileField(upload_to='resume', blank=True)
    work_status = models.BooleanField(default=False)

    # contact
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.TextField(max_length=5000, null=True, blank=True)
    location = models.ForeignKey(
        City, related_name='profiles', on_delete=models.SET_NULL, null=True, blank=True)
    emergency_contact_name = models.CharField(blank=True, max_length=150)
    emergency_phone = PhoneField(blank=True, help_text='Contact phone number')

    def send_verification_email(self):
        send_mail(
            f'Hey! Here is your {website_name} Email Verification Token',
            f' {self.mail_otp} is your Token for {website_name}',
            EMAIL_HOST_USER,
            [self.user.email],
            fail_silently=False,
        )

    def mail_otp_change(self):
        self.mail_otp = random_no

    def send_verification_SMS(self):
        message = f'Hey! Here is your {website_name} Mobile Verification Token {self.phone_otp}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} '


class Work(BaseClass):
    profile = models.ForeignKey(
        Profile, related_name='works', on_delete=models.CASCADE)
    employer = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.profile.user.username} Work at {self.employer}'


class Link(BaseClass):
    profile = models.ForeignKey(
        Profile, related_name='links', on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'{self.profile.user.username} {self.url}'


class Snippet(BaseClass):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title} : {self.body}'


class SchoolEducation(models.Model):
    profile = models.ForeignKey(
        Profile, related_name='schooleducation', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    STANDARD_CHOICES = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd '),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th')
    )
    from_standard = models.CharField(max_length=2, choices=STANDARD_CHOICES)
    to_standard = models.CharField(max_length=2, choices=STANDARD_CHOICES)

    def __str__(self):
        return f'{self.school.name} '


class Contact(BaseClass):
    profile = models.ForeignKey(
        Profile, related_name='contacts', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=100)
    soft_delete = models.BooleanField(default=False)


class Banner(BaseClass):
    """
        Side Banners that are site wide annoucements of updates and new features or blogposts
    """
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True)
