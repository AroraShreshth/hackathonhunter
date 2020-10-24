from rest_framework import serializers
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation, Contact, Banner
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

        email = validated_data['email']
        email_user_count = User.objects.filter(email=email).count()
        if email_user_count > 0:
            raise serializers.ValidationError(
                {'email': ['Account with this email already exists']})

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


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.owner.username')

    class Meta:
        model = Work
        fields = ['url', 'id', 'employer', 'role', 'start', 'end',
                  'currently_working', 'description', 'url', 'profile']
        extra_kwargs = {
            'id': {'read_only': True},
            'url': {'read_only': True},
        }


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.owner.username')

    class Meta:
        model = Link
        fields = ['id', 'url', 'profile']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class SkillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skill
        fields = ['url', 'id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


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
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'state': {'read_only': True},
        }


class InstituteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Institute
        fields = ['url', 'id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
        }


class FieldofStudySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FieldofStudy
        fields = ['url', 'id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
        }


class SchoolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = School
        fields = ['url', 'id', 'name', 'state',
                  'district', 'region', 'pincode', 'year_found', 'principal_name', 'status']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
        }


class ProfileSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    works = WorkSerializer(many=True, read_only=True)
    skill = SkillSerializer(many=True, read_only=True)
    field_of_study = FieldofStudySerializer()
    institute = InstituteSerializer()
    location = CitySerializer()

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'image', 'dob', 'gender', 'degree_type', 'institute', 'field_of_study',
                  'grad_year', 'course_length', 'resume', 'works', 'skill', 'links', 'location', 'address', 'emergency_contact_name',
                  'emergency_phone', 'shirt_size', 'published',
                  'verification_mail_sent', 'setup', 'mail_is_verified', 'phone_is_verified']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_no']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'name', 'description', 'active', 'link']
        extra_kwargs = {
            'id': {'read_only': True},
        }
