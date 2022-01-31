from django.db import models
from django.db.models.fields import CharField
import os
from twilio.rest import Client

# Create your models here.
class Event_Registration(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=30, unique=True)
    desc = models.TextField()
    location=models.CharField(max_length=20)
    from_date=models.DateField(null=True)
    from_time=models.TimeField(null=True)
    to_date=models.DateField(null=True)
    to_time=models.TimeField(null=True)
    last_date=models.DateField(null=True)
    last_time=models.TimeField(null=True)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.event_name

class Participant_Registration(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    tel=models.CharField(max_length=10)
    email=models.EmailField()
    select_event=models.CharField(max_length=30)
    type=models.CharField(max_length=20)
    num=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together=('select_event', 'email')