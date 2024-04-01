from .models import cars
from rest_framework import serializers

class carserializers(serializers.ModelSerializer):
    class meta:
        model= cars
        fields = '__all__'