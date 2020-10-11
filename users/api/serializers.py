from rest_framework import serializers
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('title', 'body', 'created_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'is_staff']


class CitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = City
        fields = ['url', 'id', 'name', 'state']


class InstituteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Institute
        fields = ['url', 'id', 'name']


class FieldofStudySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FieldofStudy
        fields = ['url', 'id', 'name']


class SchoolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = School
        fields = ['url', 'id', 'name', 'state', 'district', 'region']


class SkillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skill
        fields = ['url', 'id', 'name']
