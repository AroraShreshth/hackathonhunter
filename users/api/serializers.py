from rest_framework import serializers
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    """
        User Serializer Class
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    """
        Serializer for Registering Users on App
    """

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        validated_data = self.validated_data
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )

        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError(
                {'password': ['Both Passwords must match']})
        user.set_password(validated_data['password'])
        user.save()
        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


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
