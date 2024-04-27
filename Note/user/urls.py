from django.urls import path
from . import views


urlpatterns=[
    path("register/",views.register,name = "register"),
    path("login/",views.Login,name="user login"),
    path("logout/",views.logaut.as_view(),name="logaut")
]