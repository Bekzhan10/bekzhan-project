from django.test import TestCase
from poll.models import *
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class method.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse("Bekzhan"=="Bekzhan2")


    def test_false_is_true(self):
        print("Method: test_false_is_true")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two")
        self.assertEquals(1+1,2)

    def test_is_equal_to_three(self):
        post = Posts();
        self.assertFalse(post.one_plus_two()==2)
