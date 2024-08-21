#Se crea archivo test.py para guardar en este las pruebas que se le realizaran a cada modelo

from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    
    #Se define un test para que cree un usuario a manera de test, en este caso se daran valores para user y password
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('12345'))
