from django.urls import path, re_path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("books", views.BookesViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "libraries", views.LibrariesViewSet.as_view({"get": "list", "post": "create"})
    ),
    path(
        "library-books",
        views.LibraryBooksViewSet.as_view({"get": "list", "post": "create"}),
    ),
    re_path(
        r"library-activity/(?P<user_id>[0-9]+)/$",
        views.LibraryActivityViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "library-activity",
        views.LibraryActivityViewSet.as_view({"get": "list", "post": "create"}),
    ),
]
