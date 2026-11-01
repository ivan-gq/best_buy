import products

class Store:
    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        active_products = []
        for product in self.products:
            if product.active == True:
                 active_products.append((product))
        return active_products

    def order(self, shopping_list) -> float:
        total_price = 0.0
        
        for product, quantity in shopping_list:
            if product in self.products:
                if product.get_quantity() >= quantity:
                    total_price += product.buy(quantity)
                else:
                    raise ValueError(f"Not enough quantity")
            else:
                raise ValueError(f"Not available in the store")
        return total_price


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250),
            ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))