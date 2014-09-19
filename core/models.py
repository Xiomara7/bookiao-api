from django.db import models

WEEKDAYS = [
  (1, _("Monday")),
  (2, _("Tuesday")),
  (3, _("Wednesday")),
  (4, _("Thursday")),
  (5, _("Friday")),
  (6, _("Saturday")),
  (7, _("Sunday")),
]

# TODO: Business, Employee and Client should extend this guy
# TODO: This guy should be my base User at the project level
# TODO: Maybe inherit from AbstractBaseUser?
class BookiaoUser(models.Model):


class Business(models.Model):
  """
  Model for each Business User
  """
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  manager_name = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=50)
  phone_number = models.PhoneNumberField()
  # TODO: Maybe this should be saved in a different way?
  location = models.CharField(max_length=100)

class BusinessHours(models.Model):
  """
  Model to save hours a business is open per day.
  """
  business = models.ForeignKey(Business)
  weekday = models.IntegerField(choices=WEEKDAYS)
  from_hour = models.TimeField()
  to_hour = models.TimeField()

  class Meta:
    unique_together = ('business', 'weekday',)

class Employee(models.Model):
  """
  Model for each Employee User
  """
  name = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=50)
  phone_number = models.PhoneNumberField()
  business = models.ForeignKey(Business)
  services = models.ManyToManyField('Services')

class EmployeeHours(models.Model):
  """
  Model to save hours an employee works during a given day.
  """
  employee = models.ForeignKey(Employee)
  weekday = models.IntegerField(choices=WEEKDAYS)
  from_hour = models.TimeField()
  to_hour = models.TimeField()
  lunch_hour_start = models.TimeField()
  lunch_hour_end = models.TimeField()

  class Meta:
    unique_together = ('employee', 'weekday',)

class Services(models.Model):
  """
  Model to save the distinct services offered by employees
  """
  name = models.CharField(max_length=50)
  duration_in_minutes = models.CharField(max_length=3)

class Appointments(models.Model):
  """
  Model to save each appointment made through Bookiao
  """
  day = models.DateField()
  time = models.TimeField()
  services = models.ManyToManyField(Services)
  employee = models.ForeignKey(Employee)
  client = models.ForeignKey('Client')

class Client(models.Model):
  """
  Model for each Client User
  """
  name = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=50)
  phone_number = models.PhoneNumberField()
