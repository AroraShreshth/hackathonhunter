from django.db import models
from django.contrib.auth.models import User
from comp.models import Event
from users.models import Profile, BaseClass, Skill
# Create your models here.


class Quiz(BaseClass):
    # About Quiz
    name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comp = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    # profile used a proxy model for User
    participants = models.ManyToManyField(Profile)

    # Time -
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    time_for_each_question = models.PositiveSmallIntegerField(default=0)
    timed_question = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Question(BaseClass):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    name = models.TextField(max_length=500)
    TYPES = (
        ('MCQ', 'Multiple Choice Question'),  # Radio Buttons
        ('TF', 'True/False'),  # True False
        ('MC', 'Multi Choice'),  # CheckBoxes
    )
    types = models.CharField(max_length=3, choices=TYPES)

    def __str__(self):
        return f'{self.name}'


class Option(BaseClass):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Response(BaseClass):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    true_false = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.question.name} {self.user.username}'
