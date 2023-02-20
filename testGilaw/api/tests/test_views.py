from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/')
        self.assertEqual(response.status_code, 200)
