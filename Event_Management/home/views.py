from mailbox import ExternalClashError
from time import timezone
from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from home import models
from datetime import date, datetime
import pytz
from twilio.rest import Client

# Create your views here.
def home(request):
     return render(request, 'home.html')

def event_r(request):
     try:
          if request.method=="POST":
               event_name=request.POST['event_name']
               desc=request.POST['desc']
               location=request.POST['location']
               from_date=request.POST['from_date']
               from_time=request.POST['from_time']
               to_date=request.POST['to_date']
               to_time=request.POST['to_time']
               last_date=request.POST['last_date']
               last_time=request.POST['last_time']
               email=request.POST['email']
               password=request.POST['password']

               if from_date<to_date:
                         data=models.Event_Registration(event_name=event_name, desc=desc, location=location, from_date=from_date,
                         from_time=from_time, to_date=to_date, to_time=to_time, last_date=last_date, last_time=last_time, email=email, password=password)
                         data.save()
                         message='Your Event Registration is completed!.\n\nEvent ID: '+ str(data.id) + '\nEvent Name: '+event_name+'\nYou can also review the participation in your event using our portal.\nThank you for registering your event with us.\n\nEvent Manager Web App'

                         send_mail(
                              'Event Registered',
                              message,
                              'Your Email',
                              [email],
                              fail_silently=False
                         )
                         
               elif from_date==to_date:
                    if from_time<to_time:
                         data=models.Event_Registration(event_name=event_name, desc=desc, location=location, from_date=from_date,
                         from_time=from_time, to_date=to_date, to_time=to_time, last_date=last_date, last_time=last_time, email=email, password=password)
                         data.save()
                         message='Your Event Registration is completed!.\n\nEvent ID: '+ str(data.id) + '\nEvent Name: '+event_name+'You can also review the participation in your event using our portal.\nThank you for registering your event with us.\n\nEvent Manager Web App'
                         send_mail(
                              'Event Registered',
                              message,
                              'Your Email',
                              [email],
                              fail_silently=False
                         )
                    else:
                         messages.error(request, "Please enter valid Time.", extra_tags='time')
                         return redirect('/event_r')

               else:
                    messages.error(request, " Please enter valid Date.", extra_tags='date')
                    return redirect('/event_r')

               messages.success(request, " Your Event is registered.", extra_tags='event')
               return redirect('/event_r')
          return render(request, 'event_r.html')
          
     
     except:
          messages.success(request, " Event Name is already registered. Please use another Event Name", extra_tags='email')
          return redirect('/event_r')


def participant_r(request):
    
     filter_events=[]
     for event in models.Event_Registration.objects.all():
          if event.last_date > date.today():
               filter_events.append(event)
          elif event.last_date==date.today() and event.last_time > datetime.now().time():
               filter_events.append(event)
     return render(request, 'participant_r.html',{'events':filter_events})

def participant(request):
     try:
          if request.method=="POST":
               name=request.POST['name']
               tel=request.POST['tel']
               email=request.POST['email']
               select_event=request.POST['select_event']
               type=request.POST['type']
               num=request.POST['num']
               data=models.Participant_Registration(name=name, tel=tel, email=email, select_event=select_event, type=type,
               num=num)
               data.save()
               print(data.id)
               allevents=models.Event_Registration.objects.all()
               obj=allevents.get(event_name=select_event)
               try:
                    account_sid = "Your account_sid"
                    auth_token = "Your auth_token"
                    client = Client(account_sid, auth_token)
                    sms = client.messages.create(
                                                  body='Thank you '+name+' for registering your participation with us.\n\n'+ 'Participant ID: '+ str(data.id)+ '\nEvent Name: ' +select_event+'\nDate: '+str(obj.from_date)+' - '+str(obj.to_date)+'\nTime: '+str(obj.from_time)+' - '+str(obj.to_time)+'\nParticipation Type: '+type+'\nNo. of people: '+num+'\n\nEvent Manager Web App',
                                                  from_='Your phone number',
                                                  to=[tel],
                                             )
               except:
                    messages.error(request, " Please use a Twilio verfied mobile number.", extra_tags='number')
                    return redirect('/participant_r/participant/') 
                    

               message='Thank you '+name+' for registering your participation with us.\n\n'+ 'Participant ID: '+ str(data.id)+ '\nEvent Name: ' +select_event+'\nDate: '+str(obj.from_date)+' - '+str(obj.to_date)+'\nTime: '+str(obj.from_time)+' - '+str(obj.to_time)+'\nParticipation Type: '+type+'\nNo. of people: '+num+'\n\nEvent Manager Web App' 
               send_mail(
                    'Participant Registered',
                    message,
                    'Your Email',
                    [email],
                    fail_silently=False
               )
               
               messages.success(request, " Your Participation is registered.", extra_tags='participant')
               return redirect('/participant_r/participant/')          
          filter_events=[]
          for event in models.Event_Registration.objects.all():
               if event.last_date > date.today():
                    filter_events.append(event)
               elif event.last_date==date.today() and event.last_time > datetime.now().time():
                    filter_events.append(event)
          
               
          return render(request, 'participant.html', {'events':filter_events})
     except:
          messages.success(request, " Email is already registered. Please use another Email address", extra_tags='email')
          return redirect('/participant_r/participant/')


def dashboard(request):
     try:
          if request.method=="POST":
               event_id=request.POST['event_id']
               host_password=request.POST['host_password']
               allevents=models.Event_Registration.objects.all()
               obj=allevents.get(pk=event_id)
               allparticipants=models.Participant_Registration.objects.filter(select_event=obj.event_name)
               if obj.password==host_password:
                    if allparticipants.count()==0:
                         messages.error(request, "No Participant have registered for "+obj.event_name+" yet...", extra_tags='no')
                         return redirect('/event_dashboard/')
                    else:
                         return render(request, 'event_dashboard.html', {'participants':allparticipants})

               else:
                    messages.error(request, "Invalid Credentials", extra_tags='credentials')
                    return redirect('/event_dashboard/')
          return render(request, 'event_dashboard.html')


     except:
          messages.error(request, "Invalid Credentials", extra_tags='credentials')
          return redirect('/event_dashboard/')
          
     
