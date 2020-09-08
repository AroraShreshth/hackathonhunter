from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import send_mail
import uuid
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit import ImageSpec


class BaseClass(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4().hex[:15],
        editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Institute(BaseClass):
    name = models.CharField(max_length=300)


class FieldofStudy(BaseClass):
    name = models.CharField(max_length=300)


class Skill(BaseClass):
    name = models.CharField(max_length=300)


class Profile(BaseClass):

    # Logical Stuff
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isverified = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    # About User
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=5000, null=True, blank=True)

    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 80})
    SHIRT_SIZES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X Large'),
        ('XXL', 'XX Large'),
        ('XXXL', 'XXX Large'),
    )
    shirt_size = models.CharField(max_length=4, choices=SHIRT_SIZES)

    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('T', 'Transgender'),
        ('P', 'Prefer Not To Say'),
        ('N', 'Non Binary,Gender Queer or gender non-confirming')
    )
    shirt_size = models.CharField(max_length=1, choices=GENDER)

    # Education

    no_formal_education = models.BooleanField(default=False)

    DEGREE_TYPE = (
        ('Associate', 'Associate'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
        ('High School', 'High School')
    )

    degree_type = models.CharField(max_length=12, choices=DEGREE_TYPE)
    institute = models.ForeignKey(Institute, on_delete=models.PROTECT)
    field_of_study = models.ForeignKey(FieldofStudy, on_delete=models.PROTECT)

    grad_year = models.DateTimeField()

    # Experience
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)

    def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.user.username, filename)
    resume = models.FileField(upload_to=user_directory_path)
    work_status = models.BooleanField(default=False)

    # contact
    phone = PhoneField(blank=True, help_text='Contact phone number')
    emergency_contact_name = models.CharField(blank=True, max_length=150)
    emergency_phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Work(BaseClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    employer = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(null=True)
    url = models.URLField(blank=True)


class Links(BaseClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.URLField()
