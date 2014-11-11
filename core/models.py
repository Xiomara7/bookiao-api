# -*- coding: utf-8 -*-

from django.db import models

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


WEEKDAYS = [
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
]

class BookiaoUserManager(BaseUserManager):

  def _create_user(self, email, name, phone_number, password, is_staff, is_superuser, **extra_fields):
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(email=email, name=name, phone_number=phone_number,
                        is_staff=is_staff, is_superuser=is_superuser,
                        is_active=True, date_joined=now, last_login=now,
                        **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, name=None, phone_number=None, password=None, **extra_fields):
    return self._create_user(email, name, phone_number, password, False, False, **extra_fields)

  def create_superuser(self, email, name, phone_number, password, **extra_fields):
    return self._create_user(email, name, phone_number, password, True, True, **extra_fields)


class BookiaoUser(AbstractBaseUser):
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=10)

  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'phone_number']

  objects = BookiaoUserManager()

  def get_full_name(self):
    return self.name

  def get_short_name(self):
    return self.name

@python_2_unicode_compatible
class Business(models.Model):
  """
  Model for each Business User
  """
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=10)
  manager_name = models.CharField(max_length=50)
  # TODO: Maybe this should be saved in a different way?
  location = models.CharField(max_length=100)

  def __str__(self):
    return unicode(self.name)


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

@python_2_unicode_compatible
class Employee(models.Model):
  """
  Model for each Employee User
  """
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=10)
  business = models.ForeignKey(Business)
  services = models.ManyToManyField('Service')

  def __str__(self):
    return unicode(self.name)

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

@python_2_unicode_compatible
class Service(models.Model):
  """
  Model to save the distinct services offered by employees
  """
  name = models.CharField(max_length=50)
  duration_in_minutes = models.CharField(max_length=3)

  def __str__(self):
    return "%s - %s minutos" % (unicode(self.name), self.duration_in_minutes)

@python_2_unicode_compatible
class Appointment(models.Model):
  """
  Model to save each appointment made through Bookiao
  """
  day = models.DateField()
  time = models.TimeField()
  services = models.ManyToManyField(Service)
  employee = models.ForeignKey(Employee)
  client = models.ForeignKey('Client')

@python_2_unicode_compatible
class Client(models.Model):
  """
  Model for each Client User
  """
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=10)

  def __str__(self):
    return unicode(self.name)

