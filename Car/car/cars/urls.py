from django.urls import path
from Car import views

urlpatterns =[
    path('',views.CAR.as_view(),name= "select car"),
    path('add',views.add_car.as_view(),name= "add car"),
    path('del',views.deleteinfo.as_view(),name= "del car")

]