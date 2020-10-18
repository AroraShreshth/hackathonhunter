from invite.models import Invite
from rest_framework import serializers


class InviteSerializer(serializers.ModelSerializer):
    """
        Invite Serializer for Marketing Stuff
    """
    class Meta:
        model = Invite
        fields = ['code', 'name', 'modified_date']
        extra_kwargs = {
            'code': {'read_only': True},
            'name': {'read_only': True},
            'modified_date': {'read_only': True},
        }


class UserInviteSerializer(serializers.Serializer):
    """
        Invite Serializer for Verification Purpose
    """
    code = serializers.CharField(max_length=8)
