from django.shortcuts import render

from rest_framework.views import APIView
from .models import cars
from .serializers import carserializers
from rest_framework.response import Response

class CAR (APIView):
    def get(self,request):
        data = cars.objects.all()
        serializer = carserializers(data,context={"request":request},many = True)
        return Response(serializer.data)
    
class add_car(APIView):
    data = cars.objects.all()
    def post(self,request):
        serializer= carserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class deleteinfo(APIView):
    def delete(self,request,pk):
        event = cars.objects.get(pk=pk)
        event.delete
        return Response("successful")

