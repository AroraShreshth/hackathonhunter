from django.db import models

# Create your models here.

from users.models import BaseClass
from django.contrib.auth.models import User


class IssueType(BaseClass):
    # The Type of Issue that has been reported to the system
    name = models.CharField(max_length=300)


class Issue(BaseClass):
    title = models.CharField(max_length=300)
    detail = models.TextField()
    posted_by = models.ForeignKey(
        User,  on_delete=models.SET_NULL, null=True)

    is_type = models.ForeignKey(
        IssueType, on_delete=models.PROTECT, null=True, blank=True)

    ISSUE_STATUS = (
        ('unreviewed', 'ureviewed'),
        ('under review', 'under review'),
        ('accepted', 'accepted'),
        ('pending', 'pending'),
        ('workinprogress', 'workinprogress'),
        ('denied', 'denied'),
        ('future-release', 'future-release')
    )
    status = models.CharField(
        max_length=25, choices=ISSUE_STATUS, default='unreviewed')

    response_comment = models.TextField()
