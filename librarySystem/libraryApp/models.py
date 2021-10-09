from django.db import models

from django.contrib.auth.models import User

BOOK_IN = "BOOK_IN"
BOOK_OUT = "BOOK_OUT"
ACTIVITY_CHOICES = ((BOOK_IN, "in"), (BOOK_OUT, "out"))


class Libraries(models.Model):
    name = models.CharField(
        max_length=256, null=False, blank=False, help_text="Enter Library Name here"
    )
    city = models.CharField(
        max_length=256, null=False, blank=False, help_text="Enter Library City Here"
    )
    state = models.CharField(
        max_length=256, null=False, blank=False, help_text="Enter Library State Here"
    )
    postal_code = models.CharField(
        max_length=256, help_text="Enter Library Postal code Here"
    )


class Books(models.Model):
    title = models.CharField(
        max_length=256, null=False, blank=False, help_text="Book title"
    )
    auther_name = models.CharField(
        max_length=256, null=False, blank=False, help_text="Auther name"
    )
    isbn_number = models.CharField(
        max_length=256, null=False, blank=False, help_text="Book ISBN Number"
    )
    genre = models.CharField(
        max_length=256, null=True, blank=True, help_text="Book genre"
    )
    discription = models.TextField(null=True, blank=True)


class LibraryActivity(models.Model):
    activity_type = models.CharField(
        choices=ACTIVITY_CHOICES, default=BOOK_IN, max_length=256
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library_book = models.ForeignKey(
        "libraryApp.LibraryBooks", on_delete=models.CASCADE
    )
    checked_out = models.DateTimeField(auto_now_add=False)
    checked_in = models.DateTimeField(auto_now_add=False)


class LibraryBooks(models.Model):
    library = models.ManyToManyField(
        "libraryApp.Libraries",
        null=False,
        blank=False,
        verbose_name="Lirary-book pool",
        related_name="library",
    )
    book = models.ManyToManyField(
        "libraryApp.Books",
        null=True,
        blank=True,
        related_name="books",
        verbose_name="Books library have",
    )
    last_library_activity = models.ManyToManyField(
        "libraryApp.LibraryActivity",
        related_name="last_activity",
        null=True,
        blank=True,
    )
