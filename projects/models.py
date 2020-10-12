from django.db import models
from django.contrib.auth.models import User
from comp.models import Event, Prize
from users.models import BaseClass, Skill, Profile
from django.template.defaultfilters import slugify
# Create your models here.


class Project(BaseClass):
    """
        Profile Model of User is being used as a proxy model for User in likes
    """
    name = models.CharField(max_length=75)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    challenges = models.TextField(max_length=2500)
    slug = models.SlugField(max_length=200)
    users = models.ManyToManyField(User)
    skills = models.ManyToManyField(Skill)
    event = models.ForeignKey(
        Event, on_delete=models.SET_NULL, null=True, blank=True)

    published = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    under_review = models.BooleanField(default=False)
    official = models.BooleanField(default=False)
    winner = models.ForeignKey(
        Prize, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField()  # Count Both Public and private view
    likes = models.ManyToManyField(Profile)  # users can like a project

    def likes_count(self):
        return self.likes.all().count()

    def add_like(self, p):
        self.likes.add(p)  # p is profile model
        self.save()

    def remove_like(self, p):
        self.likes.remove(p)  # p is profile model
        self.save()

    def viewed(self):
        self.views = self.views + 1
        self.save()

    def __str__(self):
        return f'{self.name}'

    def save(self):
        if self._created or 'name' in self._get_changed_fields():
            self.slug = slugify(self)


class ProjectLink(BaseClass):
    """
    Just Links to where the project data
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'{self.project.name}: {url}'


class ProjectPhotos(BaseClass):
    """
        Used By Gallery in Project View 
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images')

    def __str__(self):
        return f'{self.project.name}: {image}'


class ProjectFiles(BaseClass):
    """
        Upload Presentation Files(Docs Video Anything) for the Project 
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files')

    def __str__(self):
        return f'{self.project.name}:'


class Discuss(BaseClass):
    """
        Discussion Comments to projects
        Profile Model of User is being used as a proxy model for User in likes
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=2000)
    likes = models.ManyToManyField(Profile)

    def likes_count(self):
        return self.likes.all().count()

    def add_like(self, p):
        self.likes.add(p)  # p is profile model
        self.save()

    def remove_like(self, p):
        self.likes.remove(p)  # p is profile model
        self.save()

    def __str__(self):
        return f'{self:user}'
