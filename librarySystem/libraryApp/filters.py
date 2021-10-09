from django_filters import FilterSet, CharFilter

from .models import LibraryActivity, BOOK_IN, BOOK_OUT


class ActivityFilter(FilterSet):
    """ """

    user_activity = CharFilter(method="filter_user_activity")

    class Meta:
        model = LibraryActivity
        fields = ["user_activity"]

    def filter_user_activity(self, queryset, name, value):
        if value == "check_out":
            queryset = queryset.filter(activity_type=BOOK_OUT)
        elif value == "check_in":
            queryset = queryset.filter(activity_type=BOOK_IN)

        return queryset
