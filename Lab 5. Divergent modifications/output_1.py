class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        self.type = product_type


class ProductSearcher:
    def search_product(self, query, products):
        # Пошук товару за запитом
        pass


class ProductDisplayer:
    def display_product(self, product):
        # Відображення інформації про товар
        pass


class ProductOrderer:
    def order_product(self, product, quantity):
        # Замовлення товару
        pass
