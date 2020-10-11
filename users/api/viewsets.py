from django.contrib.auth.models import User
from users.models import Snippet
from . import serializers as user_serial
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# class SnippetViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Snippet.objects.all()
#         serializers = SnippetSerializer(queryset, many=True)
#         return Response(serializers.data)


class SnippetViewSet(viewsets.ModelViewSet):

    # List , create , retreive , update, partial_update, destroy
    queryset = Snippet.objects.all()
    serializer_class = user_serial.SnippetSerializer

    # @action(methods=['get'], detail=True)
    # def newest(self, request, pk):
    #     newest = self.get_queryset().order_by('created_date').last()
    #     serializer = SnippetSerializer(newest)
    #     return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def random(self, request, pk):
        newest = self.get_queryset().order_by('?').last()
        serializer = user_serial.SnippetSerializer(newest)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serial.UserSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = user_serial.CitySerializer


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = user_serial.InstituteSerializer


class FieldofStudyViewSet(viewsets.ModelViewSet):
    queryset = FieldofStudy.objects.all()
    serializer_class = user_serial.FieldofStudySerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = user_serial.SkillSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = user_serial.SchoolSerializer
