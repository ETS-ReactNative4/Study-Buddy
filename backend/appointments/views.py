from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Appointment
from users.models import User
from .serializers import AppointmentSerializer, AppointmentCreateSerializer, AppointmentJoinSerializer


class Create(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = AppointmentCreateSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Join(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentJoinSerializer

    def join_appointment(self, appointment_id, username):
        user = User.objects.get(username=username)
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.users.add(user)
        return {
            "username": username,
            "appointment_id": appointment_id,
        }

    def post(self, request, *args, **kwargs):
        serializer_class = AppointmentJoinSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(self.join_appointment(request.data["appointment_id"], request.data["username"]), status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
