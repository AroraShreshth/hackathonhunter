from django.db import models
from users.models import BaseClass
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit import ImageSpec


class Location(BaseClass):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.city}'


class Event(BaseClass):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # Types
    is_online = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)
    official = models.BooleanField(default=False)
    women_only = models.BooleanField(default=False)

    # Image Data
    image = models.ImageField(
        default='event_logo/default.jpg', upload_to='event_logo')

    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 80})
    cover_image = models.ImageField(
        default='event_cover/default.jpg', upload_to='event_cover')
    cover_image_thumb = ImageSpecField(source='cover_image',
                                       processors=[ResizeToFill(150, 150)],
                                       format='JPEG',
                                       options={'quality': 80})
    # Location
    Location = models.ForeignKey(
        Location, null=True, blank=False, on_delete=models.PROTECT)
    address = models.CharField(max_length=300, blank=True)
    longitute = models.DecimalField(
        null=True, blank=True, max_digits=8, decimal_places=3)
    latitute = models.DecimalField(
        null=True, blank=True, max_digits=8, decimal_places=3)

    women_only = models.BooleanField(default=False)
    # participant stuff
    approx_particpants = models.PositiveIntegerField(default=200)

    team_size = models.SmallIntegerField(default=4)
    team_min = models.SmallIntegerField(default=2)

    winner_announced = models.BooleanField(default=False)

    # Emails Time
    reminder_email_sent_at = models.DateTimeField(null=True, blank=True)
    rsvp_email_sent_at = models.DateTimeField(null=True, blank=True)
    reminder_email_sent_at = models.DateTimeField(null=True, blank=True)
    feedback_reminder_sent_at = models.DateTimeField(null=True, blank=True)

    # Email Messgaes Content
    not_accepeted_message = models.TextField(blank=True)
    waitlist_message = models.TextField(blank=True)
    accepted_message = models.TextField(blank=True)

    # Links
    website = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    coc = models.URLField(blank=True)

    organiser_admin = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'


class Judge(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    only_speaker = models.BooleanField(default=False)
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    detail = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(
        default='judge_profile/default.jpg', upload_to='judge_profile')


class FAQ(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=500)


class SponsorType(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    priority = models.SmallIntegerField()
    size = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.event.name} : {self.name}'


class Sponsor(BaseClass):
    type = models.ForeignKey(SponsorType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics')
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 80})

    def __str__(self):
        return f'{self.type.event.name} : {self.name}'


class PrizeType(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    priority = models.SmallIntegerField()
    size = models.SmallIntegerField(blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.event.name} : {self.name}'


class Prize(BaseClass):
    type = models.ForeignKey(PrizeType, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, blank=True)

# Models Left to make
#  1. App (Application)(Status Making)
#       Status
#       a. rejected
#       b. waitlisted
#       c. accepted
#       d. under review
#       e. Applied
#       f. checkedin
#  Model Logger for all above Events
#  Create Email Field for Judge description for mailing
#  ( log all emails on DB )
#
#  4. EventTeam and Access Control with Role Access
#  5. AppTeam (w/ Option to reject individual Memebers )
#  2. Projects/Submissions Models
#  3. Feedback Model Logic
#
