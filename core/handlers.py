from os import getenv

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Appointment

from twilio.rest import TwilioRestClient
client = TwilioRestClient()

@receiver(post_save, sender=Appointment)
def notify_new_appointment(sender, **kwargs):
  appointment = kwargs['instance']
  if kwargs['created'] and getenv('PRODUCTION') == "True":
    employee_message = """ Bookiao! Tienes cita %s a las %s. El cliente es %s con numero de telefono %s. """ % (appointment.day.strftime('%b %d, %Y'), appointment.time.strftime('%I:%M %p'), appointment.client.name, appointment.client.phone_number)
    client_message = """ Bookiao! Tienes cita %s a las %s. Tu barbero es %s con numero de telefono %s. """ % (appointment.day.strftime('%b %d, %Y'), appointment.time.strftime('%I:%M %p'), appointment.employee.name, appointment.employee.phone_number)

    message = client.messages.create(to=appointment.employee.phone_number, from_=settings.TWILIO_NUMBER, body=employee_message)
    message = client.messages.create(to=appointment.client.phone_number, from_=settings.TWILIO_NUMBER, body=client_message)

