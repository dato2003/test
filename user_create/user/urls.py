from django.urls import path
from . import views

urlpatterns=[

    path("register/",views.Register.as_view(),name='user register'),
    path("login/",views.Login.as_view(),name="user login"),
    path("logout/",views.Logout.as_view(),name="user logaut"),
    path("note/",views.Notecreate.as_view(),name=" note list"),
    path("create/note",views.NoteCreate.as_view(),name="create note"),
    path("note/mg/<int:pk>",views.NotesManage.as_view(),name="manage note")

]