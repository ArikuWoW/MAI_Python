import logging
from datetime import datetime

logging.basicConfig(filename='warehouse.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class Product():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def plus_quantity(self, amount):
        self.quantity += amount

    def minus_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            logging.info(f"Уменьшено количество товара '{self.name}' на {amount}. Новое количество: {self.quantity}")
            return True
        else:
            logging.warning(f"Недостаточно товара '{self.name}' для уменьшения на {amount}. Доступно: {self.quantity}")
            return False

    def calc_price(self, amount):
        return self.quantity * self.price

class Warehouse(Product):
    def __init__(self):
        self.products = {}

    def remove_products(self, product):
        if product.name in self.products:
            self.products[product.name].increase_quantity(product.quantity)
        else:
            self.products[product.name] = product
            logging.info(f"Добавлен новый товар '{product.name}' на склад. Количество: {product.quantity}, Цена: {product.price}")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            logging.info(f"Товар '{product_name}' удалён со склада.")
        else:
            logging.warning(f"Попытка удаления несуществующего товара '{product_name}'.")

    def calculate_total_value(self):
        total_value = sum(product.calculate_cost() for product in self.products.values())
        logging.info(f"Рассчитана общая стоимость товаров на складе: {total_value}")
        return total_value


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []

    def sell_product(self, warehouse, product_name, quantity):
        if product_name in warehouse.products:
            product = warehouse.products[product_name]
            if product.decrease_quantity(quantity):
                sale_amount = quantity * product.price
                self.sales_report.append((product_name, quantity, sale_amount))
                logging.info(f"Продавец '{self.name}' продал {quantity} единиц товара '{product_name}' на сумму {sale_amount}")
                return sale_amount
        logging.warning(f"Неудачная попытка продажи товара '{product_name}' в количестве {quantity}")
        return 0

    def generate_sales_report(self):
        print("Отчёт о продажах:")
        for product_name, quantity, sale_amount in self.sales_report:
            print(f"Товар: {product_name}, Количество: {quantity}, Выручка: {sale_amount}")
        total_revenue = sum(sale[2] for sale in self.sales_report)
        print(f"Общая выручка: {total_revenue}")
        logging.info(f"Сформирован отчёт о продажах продавцом '{self.name}' на общую сумму {total_revenue}")


warehouse = Warehouse()
warehouse.remove_product(Product("Телефон", 50, 15000))
warehouse.remove_product(Product("Ноутбук", 20, 60000))
warehouse.remove_product(Product("Наушники", 100, 2000))


seller = Seller("Иван")


seller.sell_product(warehouse, "Телефон", 5)
seller.sell_product(warehouse, "Наушники", 20)


seller.generate_sales_report()


total_value = warehouse.calculate_total_value()
print(f"Общая стоимость товаров на складе: {total_value}")