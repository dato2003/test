from django.http import HttpResponse
from .models import Event

def calendar_info(request):
    latest_event = Event.objects.latest('date')
    return HttpResponse(str(latest_event))

