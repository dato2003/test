from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('Book.urls')),
    path('reader/', include('Reader.urls')),
]
