from django.test import TestCase, Client
from .models import Item

# Create your tests here.

class mainTest(TestCase):
    def setUp(self):
        self.customer = Client()
        self.item = Item.objects.create(
            name='Test Item',
            amount=5,
            description='This is a test item.',
            price=30000
        )

    def test_main_url_is_exist(self):
        response = self.customer.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.customer.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_item_creation(self):
        item = Item.objects.get(name='Test Item')
        self.assertEqual(item.amount, 5)
        self.assertEqual(item.description, 'This is a test item.')
        self.assertEqual(item.price, 30000)

    def test_item_list_view(self):
        response = self.customer.get('')
        self.assertContains(response, 'Test Item')
