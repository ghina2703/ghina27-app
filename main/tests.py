from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item

class MainViewTest(TestCase):
    def setUp(self):
        # Membuat user dummy untuk pengujian login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.item = Item.objects.create(name='Test Item', user=self.user)

    def test_create_item_view(self):
        response = self.client.get(reverse('main:create_item'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_item.html')

    def test_add_item_view(self):
        response = self.client.post(reverse('main:add_item', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)  # 302 adalah redirect status code

    def test_reduce_item_view(self):
        response = self.client.post(reverse('main:reduce_item', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_item_view(self):
        response = self.client.post(reverse('main:delete_item', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)

    def test_register_view(self):
        response = self.client.get(reverse('main:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view(self):
        response = self.client.get(reverse('main:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('main:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect setelah logout

    def test_show_xml_view(self):
        response = self.client.get(reverse('main:show_xml'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

    def test_show_json_view(self):
        response = self.client.get(reverse('main:show_json'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_show_xml_by_id_view(self):
        response = self.client.get(reverse('main:show_xml_by_id', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

    def test_show_json_by_id_view(self):
        response = self.client.get(reverse('main:show_json_by_id', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_logout(self):
        self.client.logout()