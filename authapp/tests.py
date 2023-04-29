from django.core.management import call_command
from django.test import TestCase, Client

from authapp.models import ShopUser


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = ShopUser.objects.create_superuser('django', 'django@geekshop.example', 'p@$$w0rd')

        self.user = ShopUser.objects.create_user('test_user_1', 'test_user_1@example.com', 'p@$$w0rd')

        self.user_with__first_name = ShopUser.objects.create_user('test_user_2',
                                                                  'test_user_2@example.com',
                                                                  'p@$$w0rd', first_name='Тестов')

    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title'], 'магазин')
        self.assertNotContains(response, 'Пользователь', status_code=200)

        self.client.login(username='test_user_1', password='p@$$w0rd')
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)
        response = self.client.get('/')
        self.assertContains(response, 'Пользователь', status_code=200)
        self.assertEqual(response.context['user'], self.user)

    def test_cart_login_redirect(self):

        response = self.client.get('/cart/')
        self.assertEqual(response.url, '/auth/login/?next=/cart/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test_user_2', password='p@$$w0rd')
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request['PATH_INFO'], '/cart/')
        self.assertIn('Тестов', response.content.decode())

    def test_user_logout(self):

        self.client.login(username='test_user_1', password='p@$$w0rd')

        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)

        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'cartapp')
