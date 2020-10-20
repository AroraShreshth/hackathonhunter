from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from . import serializers as user_serial
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class WorkViewSet(viewsets.ModelViewSet):
    """
    A simple Viewset for listing or retrieving Work
    """

    permission_classes_by_action = {'list': [permissions.IsAdminUser],
                                    'retrieve': [permissions.IsAuthenticated]}
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = user_serial.WorkSerializer

    queryset = Work.objects.all()

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

    def create(self, request, *args, **kwargs):
        return super(WorkViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class LinkViewSet(viewsets.ModelViewSet):
    """
    A simple Viewset for listing or retrieving Link
    """
    permission_classes_by_action = {'list': [permissions.IsAdminUser],
                                    'retrieve': [permissions.IsAuthenticated]}

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = user_serial.LinkSerializer

    queryset = Link.objects.all()

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

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class SnippetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Snippet.objects.all()
    serializer_class = user_serial.SnippetSerializer

    def list(self, request):
        q = Snippet.objects.all().order_by('?')[0]
        serializer = user_serial.SnippetSerializer(q)
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
                                    'retrieve': [permissions.IsAuthenticated],
                                    'connect': [permissions.IsAuthenticated]
                                    }

    queryset = Institute.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.InstituteSerializer

    def create(self, request, *args, **kwargs):
        return super(InstituteViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(InstituteViewSet, self).list(request, *args, **kwargs)

    @action(detail=True, methods=['post'], name='connect')
    def connect(self, request, pk):
        inst = get_object_or_404(Institute.objects.all(), pk=pk)
        profile = Profile.objects.get(user=request.user)
        profile.institute = inst
        profile.save()
        return Response({'message': f' Institute {inst.name} successfully added'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FieldofStudyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated],
                                    'connect': [permissions.IsAuthenticated]
                                    }
    queryset = FieldofStudy.objects.all()
    search_fields = ['^name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.FieldofStudySerializer

    def create(self, request, *args, **kwargs):
        return super(FieldofStudyViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(FieldofStudyViewSet, self).list(request, *args, **kwargs)

    @action(detail=True, methods=['post'], name='connect')
    def connect(self, request, pk):
        fos = get_object_or_404(FieldofStudy.objects.all(), pk=pk)
        profile = Profile.objects.get(user=request.user)
        profile.field_of_study = fos
        profile.save()
        return Response({'message': f'Field of Study {fos.name} successfully added'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated],
                                    'connect': [permissions.IsAuthenticated],
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

    @action(detail=True, methods=['post'], name='connect')
    def connect(self, request, pk):
        queryset = Skill.objects.all()
        skill = get_object_or_404(queryset, pk=pk)
        request.user.profile.skill.add(skill)
        return Response({'message': f'Skill {skill.name} successfully added'})

    @action(detail=True, methods=['post'], name='disconnect')
    def disconnect(self, request, pk):
        queryset = Skill.objects.all()

        skill = get_object_or_404(queryset, pk=pk)
        pskills = request.user.profile.skill
        if pskills.filter(name=skill.name).count():
            pskills.remove(skill)
            return Response({'message': f'Skill {skill.name} successfully disconnected'})
        else:
            return Response({'message': f'Skill {skill.name} isn\'t connected to your profile'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated],
                                    }
    queryset = School.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = user_serial.SchoolSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
