from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserInviteSerializer
from invite.models import Invite
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getinvite(request):

    if request.method == 'POST':
        serializer = UserInviteSerializer(data=request.data)
        user = request.user
        data = {}

        if user.inviteused.count() > 0:
            data = {'error': 'You have already used an invite code '}
            return Response(data)

        if serializer.is_valid():

            if user.invite.code == serializer.validated_data['code']:
                data = {'error': 'You can\'t use your own invite code'}
                return Response(data)
            try:
                i = Invite.objects.get(code=serializer.validated_data['code'])
            except Exception:
                data = {'error': 'This is not a valid invite code'}
                return Response(data)

            i.usedby_user.add(user)
            data = {'sucesss': f'Invited Successfully By {user.username}'}
            return Response(data)

        else:
            data = serializer.errors
        return Response(data)
