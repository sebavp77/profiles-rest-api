from rest_framework import serializers

#########FOr user profile serializer #################3
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serliazers a name field for testing our APIView"""

    #to accept certain field
    name = serializers.CharField(max_length=10) #mximum number of characteres

################################################################################
################# Creating user profile serializer ###############################
################################################################################
class UserProfileSerializer(serializers.ModelSerializer):
    """Seralizes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password') #Fields that ww will work with
        extra_kwargs = {'password':{'write_only':True},
            'style':{'input_type':'password'}} #Customizing properties of the
        #above fields.

########## Overwriting the default function with ours ###############
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
