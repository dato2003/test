from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.reader_info, name='reader_info'),
]

