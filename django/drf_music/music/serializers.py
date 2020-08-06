from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('title', 'artist')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes th token data
    """
    token = serializers.CharField(max_length=225)
