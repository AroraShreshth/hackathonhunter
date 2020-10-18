from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import IssueTypeSerializer, IssueSerializer
from issuerep.models import IssueType, Issue
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.response import Response


class IssueTypeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated]
                                    }

    queryset = IssueType.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = IssueTypeSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class IssueViewSet(viewsets.ModelViewSet):
    """
        A simple Viewset for listing or retrieving Issue
    """
    permission_classes_by_action = {'list': [permissions.IsAuthenticated],
                                    'retrieve': [permissions.IsAuthenticated],
                                    'create': [permissions.IsAuthenticated],
                                    }

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    serializer_class = IssueSerializer

    queryset = Issue.objects.all()

    def list(self, request):
        queryset = Issue.objects.filter(posted_by=request.user)
        serializer = IssueSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Issue.objects.filter(posted_by=request.user)
        issue = get_object_or_404(queryset, pk=pk)
        serializer = IssueSerializer(
            issue, context={'request': request})
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     return super(IssueViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
