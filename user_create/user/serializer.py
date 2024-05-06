from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ["username","password"]


    def create(self,validated_data):
        username= validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create_user(username=username,password=password)

        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Notes
        fields =["id","title","body","user"]
class NoteListSerializer(serializers.ModelSerializer):
    #user =UserSerializer(read_only= True)
    class Meta:
        model = Notes
        fields=["id","title","body","user"]



