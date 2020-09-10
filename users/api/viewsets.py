from users.models import Snippet
from .serializers import SnippetSerializer
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
    serializer_class = SnippetSerializer

    # @action(methods=['get'], detail=True)
    # def newest(self, request, pk):
    #     newest = self.get_queryset().order_by('created_date').last()
    #     serializer = SnippetSerializer(newest)
    #     return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def random(self, request, pk):
        newest = self.get_queryset().order_by('?').last()
        serializer = SnippetSerializer(newest)
        return Response(serializer.data)
