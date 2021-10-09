from django.shortcuts import render

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status, viewsets

from .filters import ActivityFilter
from .models import Books, Libraries, LibraryActivity, LibraryBooks
from .serializers import (
    BooksSerializer,
    LibrariesSerializer,
    LibraryBooksSerializer,
    LibraryActivitySerializer,
)


class BookesViewSet(viewsets.ModelViewSet):
    """
    URL: /library/books
    Supported Method: GET, POST => @todo: put/patch
    EndUse: One can list or update all vailable books in database
    Return Type: application/json
    Expected response status: 200
    Input Params: None
    """

    queryset = Books.objects.all()
    # permission_classes = []    #add permissions here
    # authentication_classes = []   #add authentication classes here
    # http_method_names = ["get", "post"]    # add allowed method here
    serializer_class = BooksSerializer


class LibrariesViewSet(viewsets.ModelViewSet):
    """
    URL: /library/libraries
    Supported Method: GET, POST => @todo: put/patch/retrive
    EndUse: One can list or add Libraries in database
    Return Type: application/json
    Expected response status: 200
    Input Params: None
    """

    queryset = Libraries.objects.all()
    # permission_classes = []    #add permissions here
    # authentication_classes = []   #add authentication classes here
    # http_method_names = ["get", "post"]    # add allowed method here
    serializer_class = LibrariesSerializer


class LibraryBooksViewSet(viewsets.ModelViewSet):
    """
    URL: /library/library-books
    Supported Method: GET, POST => @todo: put/patch/retrive
    EndUse: One can list or add Libraries and books in database
    Return Type: application/json
    Expected response status: 200
    Input Params: None
    """

    queryset = LibraryBooks.objects.all()
    serializer_class = LibraryBooksSerializer


class LibraryActivityViewSet(viewsets.ModelViewSet):
    """
    URL: 1. /library/library-activity/<user_id>/?user_activity=check_out/check_in
         2. /library/library-activity?user_activity=check_out/check_in
    Supported Method: GET, POST => @todo: put/patch/retrive
    EndUse: One can list or add all activity of a user in database
    Return Type: application/json
    Expected response status: 200
    Input Params: None
    """

    queryset = LibraryActivity.objects.all()
    serializer_class = LibraryActivitySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = ActivityFilter

    def get_queryset(self):
        queryset = super(LibraryActivityViewSet, self).get_queryset()
        user_id = self.kwargs.get("user_id")
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        return queryset
