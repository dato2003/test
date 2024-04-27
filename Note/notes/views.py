from django.shortcuts import render
from .models import Notes
from.serializer import noteserializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class NoteCollectionsViews(APIView):
    permission_classes =[IsAuthenticated]
    serializer_class = noteserializer

    def get(self,request):
        notes = request.user.notes.all()
        serializer = self.serializer_class(instance=notes,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    
class NoteSingletonViews(APIView):

    permission_class =[IsAuthenticated]
    serializer_class = noteserializer

    def get (self,request,pk):
        note = get_object_or_404(Notes,pk=pk)
        serializer = self.serializer_class(instance=note)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    

    def patch(self,request,pk):
        note =get_object_or_404(Notes,pk=pk)
        serializer = self.serializer_class(data=request.data,instance=note, partial= True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    

    def delete(self,request,pk):
        note = get_object_or_404(Notes,pk=pk)
        note.delete()

        return Response(status= status.HTTP_204_NO_CONTENT)

    

    
