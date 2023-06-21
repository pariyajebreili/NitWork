from rest_framework import serializers

from account.models import User, Freelancer, Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','is_client']



class FreelanceSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"})
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs={
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"error":"password do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.is_freelancer = True
        user.save()
        Freelancer.objects.create(user=user)
        return user


class ClientSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"})
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs={
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"error":"password do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)
        return user
    
    
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomAuthTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        #data['access'] = str(refresh.access_token)
        data['user'] = UserSerializer(self.user).data
        return data