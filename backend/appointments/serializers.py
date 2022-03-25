from django.db.models import Q  # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Appointment
from users.serializers import UserSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(required=True)
    subject = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    time = serializers.DateTimeField(required=True)
    offline_mode = serializers.BooleanField(default=True, required=False)
    meeting_link = serializers.CharField(required=False)
    users = UserSerializer()
    host = UserSerializer()

    class Meta:
        model = Appointment
        fields = (
            "topic",
            "subject",
            "description",
            "date",
            "time",
            "offline_mode",
            "meeting_link",
            "users"
            "host",
        )
