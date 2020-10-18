from rest_framework import serializers
from issuerep.models import Issue, IssueType


class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class IssueSerializer(serializers.ModelSerializer):
    is_type = IssueTypeSerializer()

    class Meta:
        model = Issue
        fields = ['id', 'title', 'created_date', 'modified_date', 'is_type', 'status', 'detail',
                  'response_comment']

        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
            'status': {'read_only': True},
            'response_comment': {'read_only': True},
        }
