from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import BookiaoUser, Business, Employee, Client, Service, Appointment

class BookiaoUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()


class BusinessSerializer(serializers.ModelSerializer):

  class Meta:
    model = Business
    fields = ('id', 'email', 'name', 'phone_number', 'manager_name', 'location')


class EmployeeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Employee
    fields = ('id', 'email', 'name', 'phone_number', 'business')


class ClientSerializer(serializers.ModelSerializer):

  class Meta:
    model = Client
    fields = ('id', 'email', 'name', 'phone_number')


class ServiceSerializer(serializers.ModelSerializer):

  class Meta:
    model = Service
    fields = ('id', 'name', 'duration_in_minutes')


class AppointmentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Appointment
    fields = ('id', 'day', 'time', 'services', 'employee', 'client')


