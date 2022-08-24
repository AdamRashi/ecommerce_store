from django.test import TestCase

from store.models import Category, Product, User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="test category",
                                             slug='test-cat')

    def test_category_model_entry(self):
        """
        Test Category model proper data insertion
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='test_cat', slug='test-cat')
        User.objects.create(username='tester')
        self.data1 = Product.objects.create(category_id=1,
                                            created_by_id=1,
                                            title='test_product',
                                            slug='test-prod',
                                            price=100)

    def test_product_model_entry(self):
        """
        Test Product model proper data insertion and representation
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'test_product')
