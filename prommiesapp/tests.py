from collections import UserDict
from django.test import TestCase

from prommiesapp.models import Profile, Prommies

# Create your tests here.
class PrommiesTest(TestCase):
    def setUp(self):
        self.user = UserDict.objects.create_user(username='testuser', password='12345')
        self.prommies = Prommies.objects.create(name='test prommies', description='test description', score=0, image='images/default.png', email='g@gmail.com', url='www.google.com')

    def test_save_prommies(self):
        self.assertTrue(self.prommies.save_prommies())

    def test_delete_prommies(self):
        self.assertTrue(self.prommies.delete_prommies())

    def test_update_prommies(self):
        self.assertTrue(self.prommies.update_prommies(self.prommies))

class ProfileTest(TestCase):
    def setUp(self):
        self.user = UserDict.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, image='images/default.png', bio='This is your bio', birth_date='2020-01-01', mobile='123456789')

    def test_save_profile(self):
        self.assertTrue(self.profile.save_profile())

    def test_delete_profile(self):
        self.assertTrue(self.profile.delete_profile())

    def test_update_profile(self):
        self.assertTrue(self.profile.update_profile(self.profile))


