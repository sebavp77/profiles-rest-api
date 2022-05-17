from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

##################################################################
##################################################################
################## Creating a Custom User manager ###############
#################################################################
##################################################################
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        #checking if the email address has been provided
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email) #to make the email
        #address case insensitive
        user = self.model(email=email,name=name)#to create a new user model


    #creating a function for the password, this is part of the
    #"AbstractBaseUser" module that we have imported before
        user.set_password(password) #ecripts the password
        user.save(using=self._db) #saving the model, between parenthesis is
        #stablish the database that I want to use

        return(user)

    #Creating a superuser Function
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return(user)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    # this tells that the email field cannot have a lenght greater
    # than 255 characters and it has to be unique
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # to check if the email is activate, by default it is set to True
    is_staff = models.BooleanField(default=False) #checks if the user is
    # a staff user and has special permissions, by default it is False

    #Specifying the custom user module, it knows how to create users and
    #control users
    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #to use the email as user name
    REQUIRED_FIELDS =   ['name'] #this tells that the user should
    #specify the user name

    #Functions for django interacts with our customer used models

    #Giving to django the ability to retrieve the fullname of the
    # users
    def get_full_name(self):
        """Retrieve full name of user"""
        return (self.name)

    def get_short_name(self):
        """Retrieve short name of user"""
        return (self.name)

    #Specifying the string representation of our model
    def __str__(self):
        """Retrieve string representation of user"""
        return (self.email)
