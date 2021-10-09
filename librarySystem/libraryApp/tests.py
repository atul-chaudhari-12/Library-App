from django.test import TestCase
from rest_framework.test import APITestCase


from model_mommy import mommy


class LibraryListTest(APITestCase):
    """
    Test suite for testing Library list api
    """

    def setUp(self):
        """ """
        self.library = mommy.make_recipe("libraryApp.Libraries")
        self.url = "/library/libraries"

    def test_all_libraries(self):

        response = self.client.get(self.url)
        self.assertEqual(len(response.json()), 1)


class LibraryActivityTest(APITestCase):
    def setUp(self):
        self.user = mommy.make_recipe("libraryApp.user_recipe")
        self.activity = mommy.make_recipe(
            "libraryApp.library_activity", activity_type="BOOK_IN", user=self.user
        )
        self.all_activity_url = "/library/library-activity"
        self.all_checkin_activity = "/library/library-activity?user_activity=check_in"
        self.all_checkout_activity = "/library/library-activity?user_activity=check_out"

    def test_all_activity_records(self):

        response = self.client.get(self.all_activity_url)

        self.assertEqual(len(response.json()), 1)

    def test_check_out_activity(self):
        response = self.client.get(self.all_checkout_activity)

        self.assertEqual(len(response.json()), 0)
