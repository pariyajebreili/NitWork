from rest_framework import serializers
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from account.models import User, Student, Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','identifier','is_student']
    


class StudentSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"})
    class Meta:
        model = Student
        fields = ['username','identifier', 'password', 'password2']
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
        Student.objects.create(user=user)
        return user


class CompanySignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"})

    class Meta:
        model = Company
        fields = ['username', 'identifier', 'ceo_name', 'address', 'description', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}, 'ceo_name': {'required': True}}



    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"error":"password do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        address = validated_data.pop('address', None)
        description = validated_data.pop('description', None)
        ceo_name = validated_data.pop('ceo_name', None)
        username = validated_data.pop('username', None)
        identifier = validated_data.pop('identifier', None)
        user = User.objects.create_user(username=username, identifier=identifier,**validated_data)
        user.is_client = True
        user.save()
        company = Company.objects.create(user=user, username=username, identifier=identifier, ceo_name=ceo_name, address=address, description=description)
        return user
    


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'username', 'identifier', 'ceo_name', 'address', 'description']
    