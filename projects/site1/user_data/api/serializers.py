from rest_framework import serializers
from user_data.models import user_data

class User_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_data
        fields = ["device_id", "timestamp", "temp", "bp_systolic", "bp_diastolic","hr","spo2"]