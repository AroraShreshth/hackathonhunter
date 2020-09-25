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
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


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
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('T', 'Transgender'),
        ('P', 'Prefer Not To Say'),
        ('N', 'Non Binary,Gender Queer or gender non-confirming')
    )
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)

    # Education

    no_formal_education = models.BooleanField(default=False)

    DEGREE_TYPE = (
        ('Associate', 'Associate'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
        ('High School', 'High School')
    )

    degree_type = models.CharField(
        max_length=12, choices=DEGREE_TYPE, blank=True)
    institute = models.ForeignKey(
        Institute, on_delete=models.PROTECT, null=True, blank=True)
    field_of_study = models.ForeignKey(
        FieldofStudy, on_delete=models.PROTECT, null=True, blank=True)
    grad_year = models.DateTimeField(null=True, blank=True)

    # Experience
    skill = models.ForeignKey(
        Skill, on_delete=models.PROTECT, null=True, blank=True)

    def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.user.username, filename)

    resume = models.FileField(upload_to='resume', blank=True)
    work_status = models.BooleanField(default=False)

    # contact
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.TextField(max_length=5000, null=True, blank=True)

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

    def send_verification_SMS(self):
        message = f'Hey! Here is your {website_name} Mobile Verification Token {self.phone_otp}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} '


class Work(BaseClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    employer = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.profile.user.username} Work at {self.employer}'


class Link(BaseClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'{self.profile.user.username} {self.url}'


class Snippet(BaseClass):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title} : {self.body}'
