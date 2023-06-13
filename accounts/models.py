from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, student_id, first_name,last_name, password=None):
        """Create a new user profile"""
        if not student_id:
            raise ValueError('Users must have an student_id')

        user = self.model(student_id=student_id, first_name=first_name,last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


    objects = UserProfileManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Retrieve full name for user"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.first_name

    def __str__(self):
        """Return string representation of user"""
        return str(self.student_id)