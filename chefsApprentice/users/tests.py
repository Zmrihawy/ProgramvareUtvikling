from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User
from django.test import Client

class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        #self.u1 = User(username='user1', password='123')
        #self.u1.save()
        #self.up1 = Profile(user_id=self.u1.id)
        #self.up1.save()

    # Method to create user
    def create_user(self, username):
        user, created = User.objects.get_or_create(username=username)
        user.set_password('123')
        user.save()
        return user

    def test_profile(self):
        # creating a user with a profile
        u1 = User(username='user1', password='123')
        u1.save()
        up1 = Profile(user_id=u1.id)
        # checks that up1 is an instance of Profile
        self.assertTrue(isinstance(up1, Profile))
        # checks if up1 is equal to the user: u1.username + str('Profile')
        self.assertEqual(up1.__str__(), u1.username + ' Profile')


    def tearDown(self):
        pass





