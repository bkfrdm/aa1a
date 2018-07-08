from django.test import TestCase
from django.urls import resolve

from storage.views import storage_search
from storage.models import Supplier

# Create your tests here.


class StorageSearchTest(TestCase):
    def test_default_page_resolves_to_storage_search_view(self):
        response = resolve('/')
        self.assertEqual(response.func, storage_search)

    def test_default_page_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'storage/storage.html')

    def test_saves_POST_request_to_database(self):
        response = self.client.post('/', {'name_storage_search': 'Test data 1'})
        self.assertEqual(Suppliers.objects.count(), 1)

        saved_item = Suppliers.objects.first()
        self.assertEqua(saved_item.di, 'Test data 1')


    def test_redirects_to_storage_page_after_POST_request(self):
        response = self.client.post('/', {'name_storage_search': 'Test data 2'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

class SupplierModelTest(TestCase):
    def test_saves_and_retrieves_items(self):
        sup_one = Supplier()
        sup_one.di = 'aa1a'
        sup_one.save()

        sup_two = Supplier()
        sup_two.di = 'cc3c'
        sup_two.save()

        all_objects = Supplier.objects.all()
        self.assertEqual(all_objects.count(), 2)

        saved_sup_one, saved_sup_two = all_objects
        self.assertEqual(saved_sup_one.di, 'aa1a')
        self.assertEqual(saved_sup_two.di, 'cc3c')
