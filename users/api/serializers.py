from rest_framework import serializers
from users.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('title', 'body', 'created_date')
