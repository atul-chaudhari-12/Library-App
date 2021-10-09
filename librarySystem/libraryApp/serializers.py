from rest_framework import serializers
from .models import Books, Libraries, LibraryActivity, LibraryBooks


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Books


class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Libraries


class LibraryBooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LibraryBooks


class LibraryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LibraryActivity
