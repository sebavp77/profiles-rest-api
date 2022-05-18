from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serliazers a name field for testing our APIView"""

    #to accept certain field
    name = serializers.CharField(max_length=10) #mximum number of characteres
