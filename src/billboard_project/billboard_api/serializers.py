from rest_framework import serializers
from . import models
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('name', 'size', 'photo', 'availabilty')
