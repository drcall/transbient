from django.test import TestCase, Client
from django.contrib.auth import get_user_model

# Create your tests here.
class LoginTest(TestCase):

    # Create dummy user for tests
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username='dummyUser')
        user.set_password('TestPassword1?')
        user.save()

    # Tests login when user exists
    def test_exists(self):
        cl = Client()
        exists = cl.login(username='dummyUser', password='TestPassword1?')
        self.assertTrue(exists)

    # Tests if logout works
    def test_signout(self):
        cl = Client()
        cl.login(username='dummyUser', password='TestPassword1?')
        User = get_user_model()
        user = User.objects.get(username='dummyUser')
        cl.logout()
        self.assertFalse(user.is_anonymous)

    # Does not login if user doesn't exist
    def test_no_user(self):
        cl = Client()
        self.assertFalse(cl.login(username='dumbUser', password='TestPassword1@'))
