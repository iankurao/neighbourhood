from django.test import TestCase
from . models import *

class ProfileTestClass(TestCase):

    def setUp(self):

        self.new_profile=Profile(bio='i love basketball')
    # test for instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    # testing the save mothod
    def test_save_profile(self):
        self.new_profile.create_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)