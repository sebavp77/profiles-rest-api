from rest_framework.views import APIView
from rest_framework.response import Response
############### To create a POST method ###########################
from rest_framework import status
from profiles_api import serializers #Our created Serliazers


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
