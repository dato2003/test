
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializer

from .models import Book

from utils import redis


class liebabry(APIView):
    def get (self,request):
        cached_data = redis.get("Book")
        if cached_data:
            return Response(cached_data)
        
        data = Book.objects.all()
        serializer = serializer.Bookserilaizer(data,context={"request": request},many=True)
        redis.set("Book",serializer.data)
        return Response(serializer.data)


