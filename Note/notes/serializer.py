from rest_framework import serializers
from .models import Notes


class noteserializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = ["user"]