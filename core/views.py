from rest_framework import viewsets

from core.models import Business, Employee, Client, Service, Appointment
from core.serializers import BusinessSerializer, EmployeeSerializer, ClientSerializer, ServiceSerializer, AppointmentSerializer


class BusinessViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = Business.objects.all()
  serializer_class = BusinessSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited
  """
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer


class ClientViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = Client.objects.all()
  serializer_class = ClientSerializer


class ServiceViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited
  """
  queryset = Service.objects.all()
  serializer_class = ServiceSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited
  """
  queryset = Appointment.objects.all()
  serializer_class = AppointmentSerializer

