from rest_framework.views import APIView
from rest_framework.response import Response
############### To create a POST method ###########################
from rest_framework import status
from profiles_api import serializers #Our created Serliazers

############## To create VIEWsets ###################################
#####################################################################
from rest_framework import viewsets


############ To create profiles ViewSet ##############################
######################################################################
from profiles_api import models

################## To use permissions ############################
##################################################################
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

############# To serarch profiles #################################
#################################################################
from rest_framework import filters

############# To use token authentication and create a log in ########
####################################################################
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # I am gonna list all the features of my
        # APIView
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over yout applicatoin logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})

        ################# Creating a function to work with the serializers #######
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
##################### Creating the PUT, PATCH and DELETE functions ############
###############################################################################

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
################################# Creating a new class to use VIEWsets ############


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request, pk=None):
        """Return a Hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_updates)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello', 'a_viewset':a_viewset})

    def create(self, request, pk=None):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'hhtp_method':'GET'})

    def update(self, request,pk=None):
        """Handle updating an object"""
        return Response({'hhhtp_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})

###################### Creating a new module ViewSet ############################
#################################################################################

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #How the user will authenticate
    authentication_classes = (TokenAuthentication,)#created as touple
    #permission classes say what the user can do
    permission_classes = (permissions.UpdateOwnProfile,)

    ## to search filters
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',) #which fields we can search

### To create a log in API views
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
