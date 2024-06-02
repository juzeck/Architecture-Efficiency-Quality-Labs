class Product:
    def __init__(self, product_id, name, category, price):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Product ID: {self.__product_id}, Name: {self.__name}, Category: {self.__category}, Price: {self.__price}"


class InventoryManagement:
    def __init__(self, products):
        self.__products = products

    def print_product_details(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                print(product)

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_id):
        self.__products = [product for product in self.__products if product.product_id != product_id]

    def get_all_products(self):
        return self.__products
