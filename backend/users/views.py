from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer, UserGetAppointmentsSerializer


class Register(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class GetAppointments(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetAppointmentsSerializer

    def get_appointments(self, username: str):
        user = User.objects.get(username=username)
        appointments = user.appointments.all()
        user_appointments = []
        for appointment in appointments:
            appointment_users = []
            for user in appointment.users.all():
                appointment_users.append(user.username)
            appointment_info = {
                "topic": appointment.topic,
                "subject": appointment.subject,
                "description": appointment.description,
                "date": appointment.date,
                "time": appointment.time,
                "offline_mode": appointment.offline_mode,
                "meeting_link": appointment.meeting_link,
                "host_username": appointment.host.username,
                "place_id_field": appointment.place_id_field,
                "place": {
                    "name": appointment.place.name,
                    "info_link": appointment.place.info_link,
                    "verified": appointment.place.verified,
                    "lat": appointment.place.lat,
                    "lng": appointment.place.lng,
                },
                "users": appointment_users,
                "host": {
                    "username": appointment.host.username,
                },
            }
            user_appointments.append(appointment_info)
        return user_appointments

    def post(self, request, *args, **kwargs):
        serializer_class = UserGetAppointmentsSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(self.get_appointments(request.data["username"]), status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class GetAppointmentsNumber(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetAppointmentsSerializer

    def get_appointments_number(self, username: str):
        user = User.objects.get(username=username)
        return user.appointments.all().count()

    def post(self, request, *args, **kwargs):
        serializer_class = UserGetAppointmentsSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(self.get_appointments_number(request.data["username"]), status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
