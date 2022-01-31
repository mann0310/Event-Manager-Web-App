from django.contrib import admin
from home.models import Participant_Registration
from  home.models import Event_Registration

# Register your models here.
admin.site.register(Event_Registration)
admin.site.register(Participant_Registration)