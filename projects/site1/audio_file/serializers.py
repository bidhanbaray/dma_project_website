from rest_framework import serializers
from .models import audio_file

class audio_fileSerializer(serializers.ModelSerializer):
    class Meta():
        model = audio_file
        fields = ('device_id', 'audio_file', 'timestamp')