from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
class UserProfileView(APIView):
    """Test API View."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'

        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            size = serializer.data.get('size')
            photo = serializer.data.get('photo')
            availabilty = serializer.data.get('availabilty')
            message = 'Hello {0}'.format(name,size,photo,availabilty)
            return Response({'name':name, 'size':size, 'photo':photo,'availabilty':availabilty})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
