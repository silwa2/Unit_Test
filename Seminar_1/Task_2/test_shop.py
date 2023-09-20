import unittest

from shop import Shop, Product


class TestShop(unittest.TestCase):
    def setUp(self) -> None:
        self.shop = Shop([Product(5, 'Хлеб'),
                          Product(2, 'Молоко'),
                          Product(6, 'Яблоки')])
        self.sorted_products = [Product(2, 'Молоко'),
                                Product(5, 'Хлеб'),
                                Product(6, 'Яблоки')]
        self.most_expensive_product = Product(6, 'Яблоки')

    def test_products_in_shop(self):
        """Проверяет сразу на количество товаров и их идентичность"""
        self.assertCountEqual(self.sorted_products, self.shop.products)

    def test_get_most_expensive_product(self):
        self.assertEqual(self.most_expensive_product, self.shop.get_most_expensive_product())

    def test_sort_products_by_price(self):
        self.shop.sort_products_by_price()
        for i, product in enumerate(self.shop.products):
            self.assertEqual(self.sorted_products[i], product)


if __name__ == '__main__':
    unittest.main(verbosity=2)