from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
# from ..fakers.category import CategoryFactory
from budget_management.views.category import CategoryViewSet
from django.contrib.auth.models import User
from budget_management.models.category import Category


class TestCategoryViewSet(APITestCase):
    def setUp(self):
        super().setUp()
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    
    def tearDown(self):
        return super().tearDown()
    
    # def make_request(self, path, view, request_data, kwargs):
    #     factory = APIRequestFactory()
    #     request = factory.get('/api/your-protected-endpoint/')
    #     force_authenticate(request, user=self.user)
    #     response = self.view(request, **kwargs)



    def test_create_category(self):
        self.path = "api/v1/categories/"
        self.data = {
            'name': 'food',
            'color': 'red',
            'symbol': 'hamburger'
        }
        before_count = Category.objects.filter(created_by=self.user).count()
        request = self.factory.post(self.path, data=self.data, content_type='application/json')
        force_authenticate(request, user=self.user)
        response = CategoryViewSet.as_view({'post': 'create'})(request)
        after_count = Category.objects.filter(created_by=self.user).count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(before_count, after_count)
        category = Category.objects.filter(created_by=self.user).last()
        self.assertEqual(category.name, self.data.get('name'))
        self.assertEqual(category.color, self.data.get('color'))
        self.assertEqual(category.symbol, self.data.get('symbol'))
        self.assertEqual(print(category), self.data.get('name'))


    def test_update_category(self):
        pass

    def test_delete_category(self):
        pass
    
    def test_get_list_of_categories(self):
        pass

    def test_search_a_category(self):
        pass