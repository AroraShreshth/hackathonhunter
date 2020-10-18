from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from .serializers import UserSerializer, RegisterSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


@api_view(['POST', 'GET'])
def registerapi(request):
    if request.method == 'GET':
        data = {'message':
                'You probably shouldn\'t be medling here '}
        return Response(data)

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['email'] = user.email
            data['username'] = user.username
            data['token'] = Token.objects.get(user=user).key
        else:
            data = serializer.errors
        return Response(data)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()

        return Response({'message': 'Logged Out Succesfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def whoami(request, format=None):
    user = request.user
    content = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_active': user.is_active,
        'last_login': user.last_login,
        'date_joined': user.date_joined

        # 'auth': str(request.auth),  # None
    }
    return Response(content)


@api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, format=None):
    user = request.user
    serializer = ProfileSerializer(
        instance=user.profile, context={'request': request})
    return Response(serializer.data)

# Register API


# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     _, token = AuthToken.objects.create(user)
    #     return Response({
    #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "token": token
    #     })


# Login API
# class LoginAPI(generics.GenericAPIView):
#     pass
    # serializer_class = LoginSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data
    #     _, token = AuthToken.objects.create(user)
    #     return Response({
    #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "token": token
    #     })


# Get User API
# class UserAPI(generics.RetrieveAPIView):
#     pass

    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = UserSerializer

    # def get_object(self):
    #     return self.request.user
