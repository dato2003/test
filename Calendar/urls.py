from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_info, name='calendar_info'),
]