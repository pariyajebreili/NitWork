from rest_framework import generics, status,  permissions
from rest_framework.response import Response
from .serializers import FreelanceSignupSerializer, UserSerializer, ClientSignupSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
#from rest_framework.authtoken import ObtainAuthToken
from rest_framework.views import APIView
from .permissions1 import IsClientUser, IsFreelanceUser
from account.api import permissions1
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login

class FreelanceSignupView(generics.GenericAPIView):
    serializer_class = FreelanceSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "message" : "account created successfuly"
        })



class ClientSignupView(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message" : "account created successfuly"
        })
    



class user_LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        #print(serializer)
        serializer.is_valid(raise_exception=True)
        #print(serializer.is_valid(raise_exception=True))
        user = serializer.validated_data['user']
        login(request, user)
        return super(user_LoginAPI, self).post(request, format=None)
    


#class CustomAuthToken(TokenObtainPairView):
#    serializer_class = CustomAuthTokenSerializer
    #def post(self, request, *args, **kwargs):
    #        response = super().post(request, *args, **kwargs)
    #        token = response.data.get('access', None)
    #        if token:
    #            request.auth.delete()
    #        return response
    
    #def post(self, request, *args, **kwargs):
        #serializer = self.serializer_class(data = request.data, context = {'request':request})
        #serializer.is_valid(raise_exception = True)
        #user = serializer.validated_data['user']
        #token=Token.objects.get_or_create(user=user)
        #return Response({
        #    'token':token.key,
        #    'user_id':user.pk,
        #    'is_client':user.is_client
        #})


#@api_view(['POST'])
#@authentication_classes((TokenAuthentication,))
#def CustomAuthToken(request):
#    user = request.user
#    token = Token.objects.get(user=user)
#    return Response({
#        'token': token.key,
#        'user_id': user.pk,
#        'is_client': user.is_client
#    })



#class CustomAuthToken(TokenObtainPairView):

#    @classmethod
#    def get_token(cls, user):
#        token = get_token(user)
#        token['is_client'] = user.is_client
#        return token
    
#    def get_user(self, request):
#        user = request.user
#        if user.is_authenticated:
#            return user
#        return None
    
#    def post(self, request, *args, **kwargs):
#        response = super().post(request, *args, **kwargs)
#        token = response.data['access']
#        #token2 = response.data[get_token]
#        user = self.get_user(request)
#        a = self.get_token(user)
#        print(a)
#        if user is not None:
#            user_id = user.pk
#            is_client = user.is_client
#        else:
#            user_id = None
#            is_client = None
    
#        return Response({
#            'token': token,
#            'user_id': user_id,
#            'is_client': is_client
#        }, status=status.HTTP_200_OK)
  


#class LogoutView(APIView):
#    def post(self, request, format=None):
#        request.auth.delete()
#        return Response(status=status.HTTP_200_OK)
    



class ClientOnlyView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated&IsClientUser]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user


class FreelanceOnlyView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated&IsFreelanceUser]
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user


