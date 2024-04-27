from django.urls import path
from . import views


urlpatterns=[
    path("",views.NoteCollectionsViews.as_view()),
    path("<int:pk>/",views.NoteSingletonViews.as_view())
]