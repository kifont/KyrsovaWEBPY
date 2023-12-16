from rest_framework.test import APITestCase, APIRequestFactory
from Seats.auth_view import CustomAuthToken, RegisterUserView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthenticationAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CustomAuthToken.as_view()
        self.url = '/api-token-auth/'
        self.user = User.objects.create_user(username='kif', password='123')

    def test_authentication_success(self):
        data = {'username': 'kif', 'password': '123'}
        request = self.factory.post(self.url, data, format='json')
        token = Token.objects.create(user=self.user)
        request.META['HTTP_AUTHORIZATION'] = f'Token {token.key}'
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_failure(self):
        data = {'username': 'kif', 'password': '123'}
        request = self.factory.post(self.url, data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RegistrationAPITestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RegisterUserView.as_view()
        self.url = '/register/'

    def test_user_registration_success(self):
        data = {'username': 'kif', 'password': '123'}
        request = self.factory.post(self.url, data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='kif').exists())

    def test_user_registration_failure(self):
        existing_user = User.objects.create_user(username='kif', password='123')
        data = {'username': 'kif', 'password': '123'}
        request = self.factory.post(self.url, data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username='newuser').exists())