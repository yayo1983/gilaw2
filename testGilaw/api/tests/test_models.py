from django.test import TestCase
from ..models import TypeN, TypeNotification
from users.models import User

class ModelsTestCase(TestCase):
    def setUp(self):
        user = User.objects.filter(pk=2).first()
        typeN = TypeN.objects.create(type="SMS")
        typeN.users = user
        typeN.save()


    def test_typeN_create(self):
        typeN = TypeN.objects.get(type="SMS")
        self.assertEqual(typeN.type, 'SMS')
