from xml.dom import ValidationErr
from django.db.models import Q
from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Appointment
from users.models import User
from place.models import Place
from users.serializers import UserSerializer
from place.serializers import PlaceSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(required=True)
    subject = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_blank=True)
    date = serializers.DateField(required=True)
    time = serializers.TimeField(required=True)
    offline_mode = serializers.BooleanField(default=True, required=False)
    meeting_link = serializers.CharField(required=False)
    host_username = serializers.CharField(required=True)
    place_id_field = serializers.IntegerField(required=True)

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
            "host_username",
            "place_id_field",
        )


class AppointmentCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        user = User.objects.filter(Q(username=data['host_username']))
        place = Place.objects.filter(Q(id=data['place_id_field']))
        if not user.exists():
            raise ValidationError("username is not found.")
        if not place.exists():
            raise ValidationError("place is not found.")
        user = User.objects.get(username=data['host_username'])
        place = Place.objects.get(id=data['place_id_field'])
        Appointment.objects.create(
            topic=data['topic'],
            subject=data['subject'],
            description=data['description'],
            date=data['date'],
            time=data['time'],
            offline_mode=data['offline_mode'],
            meeting_link=data['meeting_link'],
            host_username=data['host_username'],
            host=user,
            place=place,
        )
        return data

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
            "host_username",
            "place_id_field",
        )


class AppointmentJoinSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    appointment_id = serializers.IntegerField()

    def validate(self, data):
        user = User.objects.filter(Q(username=data['username']))
        appointment = Appointment.objects.filter(Q(id=data['appointment_id']))
        if not user.exists():
            raise ValidationError("username is not found.")
        if not appointment.exists():
            raise ValidationError("appointment is not found.")
        return data

    class Meta:
        model = Appointment
        fields = ("username", "appointment_id")


class AppointmentsGetFilteredSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(allow_blank=True)
    topic = serializers.CharField(allow_blank=True)
    username = serializers.CharField(allow_blank=True)

    def validate(self, data):
        return data

    class Meta:
        model = Appointment
        fields = ('subject', 'topic', 'username')
