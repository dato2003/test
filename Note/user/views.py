from rest_framework import status
from rest_framework.response import Response
from .serializer import userserializer,userloginserialzer
from rest_framework.decorators import api_view,APIView
from django.contrib.auth import authenticate ,login,logout
from rest_framework.permissions import IsAuthenticated



@api_view(["POST"])
def register(request):
    if request.user.is_authenticated:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)
    return Response(data= serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def Login(request):
    if request.user.is_authenticated:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = userloginserialzer(data=request.data)
    if not serializer.is_valid():
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    username =serializer.validated_data["username"]
    password = serializer.validated_data["password"]

    user = authenticate(username= username,password = password)

    if user is None:
        return Response(data={"error":"invalid username or password"},status=status.HTTP_400_BAD_REQUEST)
    login(request,user)
    return Response(status=status.HTTP_200_OK)


class logaut(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        logout(request)
     
        return Response(status=status.HTTP_200_OK)
    