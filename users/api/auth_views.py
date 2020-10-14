from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token


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

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

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
class LoginAPI(generics.GenericAPIView):
    pass
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
class UserAPI(generics.RetrieveAPIView):
    pass

    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = UserSerializer

    # def get_object(self):
    #     return self.request.user
