from rest_framework import serializers
from .models import User, Playlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid', 'password']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['userid', 'title', 'description', 'songs', 'letter']
