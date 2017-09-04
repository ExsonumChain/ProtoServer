from .models import *
from rest_framework import serializers


class AudioFileSerializer(serializers.ModelSerializer):
    file = serializers.StringRelatedField()

    class Meta:
        model = AudioFile
        fields = ('file', 'length_seconds', 'size_bytes')


class StationSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField()

    class Meta:
        model = Station
        fields = ('name', 'image', 'subscription_count')


class TrackSerializer(serializers.ModelSerializer):
    audio_file = AudioFileSerializer()
    image = serializers.StringRelatedField()

    class Meta:
        model = Track
        fields = ('station', 'audio_file', 'name', 'url', 'description', 'image', 'like_count', 'report_count')

