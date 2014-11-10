from django.contrib.auth import get_user_model

from rest_framework import viewsets, status, serializers, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import BookiaoUser, Business, Employee, Client, Service, Appointment
from core.serializers import BookiaoUserSerializer, BusinessSerializer, EmployeeSerializer, ClientSerializer, ServiceSerializer, AppointmentSerializer

@api_view(['POST'])
def register(request):
  VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
  DEFAULTS = {
      # you can define any defaults that you would like for the user, here
  }
  serialized = BookiaoUserSerializer(data=request.DATA)
  if serialized.is_valid():
      user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
      user_data.update(DEFAULTS)
      user = get_user_model().objects.create_user(
          **user_data
      )
      return Response(BookiaoUserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
  else:
      return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

# View to get the user type of a user, given an email
# Returns the user's respective object (Business, Employee or Client) with
# the parameter userType holding the actual type of the user objects
@api_view(['GET'])
def user_type(request):
  email = str(request.QUERY_PARAMS['email'])

  response = {}

  userType = 'none'

  business = Business.objects.filter(email=email).values()
  if len(business) > 0:
    userType = 'business'
    response.update(business[0])

  employee = Employee.objects.filter(email=email).values()
  if len(employee) > 0:
    userType = 'employee'
    response.update(employee[0])

  client = Client.objects.filter(email=email).values()
  if len(client) > 0:
    userType = 'client'
    response.update(client[0])

  response['userType'] = userType
  return Response(response, status=status.HTTP_200_OK)

class BusinessViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows businessess to be viewed or edited.
  """
  queryset = Business.objects.all()
  serializer_class = BusinessSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = (filters.DjangoFilterBackend,)
  filter_fields = ('email',)


class EmployeeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows employees to be viewed or edited
  """
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = (filters.DjangoFilterBackend,)
  filter_fields = ('email', 'business',)


class ClientViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Clients to be viewed or edited.
  """
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = (filters.DjangoFilterBackend,)
  filter_fields = ('email', 'phone_number',)

class ServiceViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows services to be viewed or edited
  """
  queryset = Service.objects.all()
  serializer_class = ServiceSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]


class AppointmentViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows appointments to be viewed or edited
  """
  queryset = Appointment.objects.all()
  serializer_class = AppointmentSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
  filter_fields = ('employee', 'client', 'day',)
  ordering_fields = ('time', 'day',)
