from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import BookiaoUser, Business, Employee, Client, Service, Appointment

class BookiaoUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()


class BusinessSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Business
    fields = ('url', 'email', 'name', 'phone_number', 'manager_name', 'location')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Employee
    fields = ('url', 'email', 'name', 'phone_number', 'business')


class ClientSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Client
    fields = ('url', 'email', 'name', 'phone_number')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Service
    fields = ('url', 'name', 'duration_in_minutes')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Appointment
    fields = ('url', 'day', 'time', 'services', 'employee', 'client')


