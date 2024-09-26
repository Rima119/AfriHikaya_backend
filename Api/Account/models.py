from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class CustomUserManager(BaseUserManager):
   
    def create_user(self, email, password=None, **extra_fields ):
        if email is  None:
            raise TypeError('User must have an email address')
        # if username is None:
        #     raise TypeError('User must have a username')
        if password is None:
            raise TypeError('enter your password')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        if password:
            harshed_password = make_password(password)
            user.password = harshed_password
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields ):
        if email is None:
            raise TypeError('user email required')
        if password is  None:
            raise TypeError('user password required')
        
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.roles = 'Admin'
        user.save()
        return user


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    country = models.CharField(max_length=160)
    native_language = models.CharField(max_length=160)
    other_names = models.CharField(max_length=160)
    hobbies = models.CharField(max_length=255, blank=True, null=True)
    roles = models.CharField(max_length=160, blank=True, null=True)
    profile_pic_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) :
        return self.email
    
    def get_token(self):
        refresh = RefreshToken.for_user(self)

        # Add custom claims
        refresh['user_id'] = self.id
        refresh['roles'] = self.roles
        refresh['email'] = self.email

        # Return the entire refresh token object
        return refresh
