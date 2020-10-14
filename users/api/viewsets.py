from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from . import serializers as user_serial
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class WorkViewSet(viewsets.ViewSet):
    """
    A simple Viewset for listing or retrieving Work
    """
    permission_classes_by_action = {'list': [permissions.IsAdminUser],
                                    'retrieve': [permissions.IsAuthenticated]}

    def list(self, request):
        queryset = Work.objects.all()
        serializer = user_serial.WorkSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Work.objects.all()
        work = get_object_or_404(queryset, pk=pk)
        serializer = user_serial.WorkSerializer(
            work, context={'request': request})
        return Response(serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class LinkViewSet(viewsets.ViewSet):
    """
    A simple Viewset for listing or retrieving Link
    """
    permission_classes_by_action = {'list': [permissions.IsAdminUser],
                                    'retrieve': [permissions.IsAuthenticated]}

    def list(self, request):
        queryset = Link.objects.all()
        serializer = user_serial.LinkSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Link.objects.all()
        link = get_object_or_404(queryset, pk=pk)
        serializer = user_serial.LinkSerializer(
            link, context={'request': request})
        return Response(serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


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


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated]
                                    }
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


class InstituteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated]
                                    }

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


class FieldofStudyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated]
                                    }
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


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated]
                                    }

    queryset = Skill.objects.all()
    search_fields = ['^name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.SkillSerializer
    permission_classes = [IsAuthenticated]

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
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated]
                                    }
    queryset = School.objects.all()
    search_fields = ['name']
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
