from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from rest_framework.test import force_authenticate, APIClient, APIRequestFactory

from budget.models import Transaction, Account


client = Client()
api = APIClient()

class AccountTest(TestCase):

    def create_superuser_for_account_list(self, username='myuser', password='mypassword'):
        return User.objects.create_superuser(username=username, password=password)

    def create_random_user_for_account_list(self, username='myuser1', password='mypassword1'):
        return User.objects.create(username=username, password=password)

    def test_account_view_for_superuser(self):
        a = self.create_superuser_for_account_list()
        url = reverse("account-list")
        api.force_authenticate(user=a)
        response = api.get(url)
        self.assertEqual(response.status_code, 200)

    def test_account_view_for_random_user(self):
        a = self.create_random_user_for_account_list()
        url = reverse("account-list")
        api.force_authenticate(user=a)
        response = api.get(url)
        print(response.data)
        self.assertEqual(response.status_code, 403)

    def create(self, account="Clothes", category=1, description="Clothes and accessories"):
        return Account.objects.create(account=account, category=category, description=description)

    def test_account_creation(self):
        a = self.create()
        self.assertTrue(isinstance(a, Account))


    def test_account_view_for_no_user(self):
        a = self.create()
        url = reverse("account-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 403)

    def set_up(self):
        user1 = User.objects.create_user(
            username="admin123",
            password="admin123")

    def test_login(self):
        client = APIClient()
        user = client.force_authenticate(user="admin123")
        self.assertIsNone(user, None)