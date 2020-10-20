from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class BaseClass(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Transaction(BaseClass):
    """
        Coins of Transaction 
    """
    value = models.PositiveIntegerField()
    user = models.ForeignKey(User, related_name='transaction',
                             on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if user == NULL:
            return self.value
        return f'{self.value} : {self.user.username}'


class Level(BaseClass):
    """
        Level that will be given based on user activity and coins 
    """
    threshold = models.PositiveIntegerField()
    name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=300)
    logo = models.FileField(upload_to='level_logo', blank=True)
    banner = models.FileField(upload_to='level_banner', blank=True)

    def __str__(self):
        return f'{self.name} : {self.threshold}'


class Awards(BaseClass):
    """ 
        Awards Awarded to multiple Users
    """
    name = models.CharField(max_length=150)
    threshold = models.PositiveIntegerField()
    logo = models.FileField(upload_to='award_icon', blank=True)
    banner = models.FileField(upload_to='award_banner', blank=True)
    description = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'
