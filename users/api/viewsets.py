from django.contrib.auth.models import User
from users.models import Snippet
from . import serializers as user_serial
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.decorators import action


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
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated]}
    queryset = City.objects.all()
    search_fields = ['^name', '^state']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.CitySerializer

    def create(self, request, *args, **kwargs):
        return super(CityViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(CityViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class InstituteViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated]}

    queryset = Institute.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.InstituteSerializer

    def create(self, request, *args, **kwargs):
        return super(InstituteViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(InstituteViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FieldofStudyViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated]}
    queryset = FieldofStudy.objects.all()
    search_fields = ['^name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.FieldofStudySerializer

    def create(self, request, *args, **kwargs):
        return super(FieldofStudyViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(FieldofStudyViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated]}
    queryset = Skill.objects.all()
    search_fields = ['^name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.SkillSerializer

    def create(self, request, *args, **kwargs):
        return super(SkillViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(SkillViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated]}
    queryset = School.objects.all()
    search_fields = ['name']
   # search_fields = ['^name'] # For Starts with put this upper arrow char
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.SchoolSerializer

    def create(self, request, *args, **kwargs):
        return super(SchoolViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(SchoolViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
