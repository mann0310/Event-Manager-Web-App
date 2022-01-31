from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header="Admin's Dashboard"
admin.site.site_title="Admin's Dashboard"
admin.site.index_title="Welcome to this portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('event_r/', views.event_r, name="event"),
    path('participant_r/', views.participant_r, name="participant"),
    path('participant_r/participant/', views.participant, name="participant"),
    path('event_dashboard/', views.dashboard, name="dashboard"),
]