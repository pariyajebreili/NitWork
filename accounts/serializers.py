from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user profile objects"""

    class Meta:
        model = UserProfile
        fields = ('id', 'student_id', 'first_name', 'last_name')
        read_only_fields = ('id')

    def create(self, student_id, first_name,last_name, password=None):
        """Create a new user profile"""
        user = UserProfile.objects.create_user(
            student_id='student_id',
            first_name='first_name',
            last_name='last_name',
            password='password'
        )

        return user

    def update(self, instance, validated_data):
        """Update a user profile"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'student_id', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create(validated_data['student_id'], validated_data['first_name'], validated_data['last_name'])

        return user