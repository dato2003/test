from rest_framework import serializers

from Library import Book


class Bookserilaizer(serializers.ModelSerializer):
    class Meta:
        models = Book
        fields = "__all__"
        