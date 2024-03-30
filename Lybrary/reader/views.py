from django.shortcuts import render
from .models import Reader

def reader_info(request):
    if request.method == 'POST':
        data =Reader(request.POST)
        return render(request, 'thank_you.html', {'reader': data})
    return render(request, 'reader_info.html')

