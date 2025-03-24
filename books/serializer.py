from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class StudentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "description", "image")
