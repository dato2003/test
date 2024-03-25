from django.http import HttpResponse
from .models import UserProfile

def user_info(request):
    user_profile = UserProfile.objects.first() 
    return HttpResponse(f"Name: {user_profile.first_name} {user_profile.last_name}, Age: {user_profile.age()}")

