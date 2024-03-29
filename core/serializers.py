from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import BookiaoUser, Business, Employee, Client, Service, Appointment, BetaEmails

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

  time = serializers.TimeField(format='%I:%M %p', input_formats=['%I:%M %p'])

  services = serializers.SlugRelatedField(many=True, slug_field='name')
  employee = serializers.SlugRelatedField(slug_field='name')
  client = serializers.SlugRelatedField(slug_field='name')

  class Meta:
    model = Appointment
    fields = ('id', 'day', 'time', 'services', 'employee', 'client')

  def validate_time(self, attrs, source):
    # Check for appointments starting in the past
    appointments = Appointment.objects.filter(day=attrs['day'], time__lte=attrs['time'])
    this_datetime = datetime.combine(datetime.today(), attrs[source])
    for appointment in appointments:
      appointment_datetime = datetime.combine(datetime.today(), appointment.time)
      finish_time = appointment_datetime + timedelta(minutes=int(appointment.services.all()[0].duration_in_minutes))
      if finish_time > this_datetime:
        raise serializers.ValidationError("Time not available.")

    # Check for appointments starting in the future
    appointments = Appointment.objects.filter(day=attrs['day'], time__gte=attrs['time'])
    this_datetime = this_datetime + timedelta(minutes=int(attrs['services'][0].duration_in_minutes))
    for appointment in appointments:
      appointment_datetime = datetime.combine(datetime.today(), appointment.time)
      if this_datetime > appointment_datetime:
        raise serializers.ValidationError("Time not available.")

    return attrs

class BetaEmailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = BetaEmails


