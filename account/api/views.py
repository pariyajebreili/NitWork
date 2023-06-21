from rest_framework import generics, status,  permissions
from rest_framework.response import Response
from .serializers import StudentSignupSerializer, UserSerializer, CompanySignupSerializer
from .permissions1 import IsCompany, IsStudent
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated




class StudentSignupView(generics.GenericAPIView):
    serializer_class = StudentSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "message" : "account created successfuly"
        })



class CompanySignupView(generics.GenericAPIView):
    serializer_class = CompanySignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
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
    


class CompanyOnlyView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated&IsCompany]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user


class StudentOnlyView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated&IsStudent]
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
    




class StudentUpdateView(generics.UpdateAPIView):
    serializer_class = StudentSignupSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class CompanyUpdateView(generics.UpdateAPIView):
    serializer_class = CompanySignupSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

