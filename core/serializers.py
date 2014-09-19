from core.models import Business, Employee, Client, Service, Appointment
from rest_framework import serializers

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


