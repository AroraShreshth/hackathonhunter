from django.db import models
from users.models import BaseClass
from django.contrib.auth.models import User
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit import ImageSpec
from users.models import City


class Event(BaseClass):
    name = models.CharField(max_length=300)
    tagline = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=300, )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # Types
    is_online = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    official = models.BooleanField(default=False)
    women_only = models.BooleanField(default=False)
    is_team_comp = models.BooleanField(default=True)
    application_review = models.BooleanField(default=False)

    COMP_STATUS = (
        ('unreviewed', 'ureviewed'),
        ('under review', 'under review'),
        ('accepted', 'accepted'),
        ('changes required', 'changes required'),
        ('denied', 'denied'),
    )

    status = models.CharField(
        max_length=25, choices=COMP_STATUS, default='unreviewed')
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
    city = models.ForeignKey(
        City, null=True, blank=True, on_delete=models.PROTECT)
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

    class Meta:
        ordering = ['-start_date']
        unique_together = ['slug', 'name']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)


class Announcement(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    content = models.TextField()

    def __str__(self):
        return f'{self.content}'


class ApplicationQuestion(BaseClass):
    """
        Application Question
    """
    TYPES = (
        ('File', 'File'),
        ('Text', 'Text'),
        ('Boolean', 'Boolean')
    )
    required = models.BooleanField(default=True)
    types = models.CharField(choices=TYPES, default='Text', max_length=10)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    question = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.question}'


class TimelineEvent(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    important = models.BooleanField(default=False)
    date = models.DateTimeField()
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} {self.event.name} {self.date}'


class Judge(BaseClass):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    only_speaker = models.BooleanField(default=False)
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
    detail = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(
        default='judge_profile/default.jpg', upload_to='judge_profile')

    def __str__(self):
        return f"{self.name}"


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
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

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
    """
     Prizes Data and Type 
    """
    type = models.ForeignKey(PrizeType, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, blank=True)
    # Result Decleration
    awarded_to = models.ForeignKey(User, null=True, on_delete=models.PROTECT)


class EventMember(BaseClass):
    """
        Add Memebers to manage functionality provided in the organise section of the application
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    roll_name = models.CharField(max_length=200)

    public = models.BooleanField(default=True)

    overview = models.BooleanField(default=False)
    review = models.BooleanField(default=False)
    volunteer = models.BooleanField(default=False)
    #logistics = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} {self.event.name}'


class Feedback(BaseClass):
    """
        Create Feedback Question 
    """
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    question = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.question}'


# Models Left to make
#  1. App (Application)(Status Making)
#       Status
#       a. rejected
#       b. waitlisted
#       c. accepted
#       d. under review
#       e. Applied
#       f. Checkedin
#       h. Missed
#  Model Logger for all above Events
#  ( log all emails on DB )
#  4. EventTeam and Access Control with Role Access
#  5. AppTeam (w/ Option to reject individual Memebers )
#  2. Projects/Submissions Models
#  3. Feedback Model Logic
