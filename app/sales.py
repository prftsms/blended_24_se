from faker import Faker
from pprint import pprint
from dotenv import dotenv_values
from openai import OpenAI
from pathlib import Path
import json
import logging
import sys
from models import Customer, Order

config = dotenv_values(".env")
client = OpenAI(api_key=config.get('OPENAI_API_KEY'))

logging.basicConfig(
    level=logging.INFO,  # level=logging.DEBUG, # INFO, WARNING, ERROR, CRITICAL
    format="%(levelname)8s: %(message)s",
    handlers=[
        logging.FileHandler('log.log'),  # log to a file
        logging.StreamHandler(sys.stdout)  # log to console
    ],
)

fake = Faker()

class Manager:
    def __init__(self) -> None:
        self.customers = {}
        self.orders = {}

    def add_customer(self, customer: Customer) -> Customer:
        self.customers[customer.customer_id] = customer
        return customer

    def create_order(self, order: Order) -> Order:
        self.orders[order.order_id] = order
        return order

    def update_customer(self, id, name=None, phone=None, mail=None) -> None:
        if id in self.customers:
            current_customer: Customer = self.customers[id]
            if name:
                current_customer.name = name
            if phone:
                current_customer.phone = phone
            if mail:
                current_customer.mail = mail

    def update_order(self, order_id, product=None, quantity=None, price=None, status=None):
        if order_id in self.orders:
            current_order = self.orders[order_id]
            if product:
                current_order.product = product
            if quantity:
                current_order.quantity = quantity
            if price:
                current_order.price = price
            if status:
                current_order.status = status

    def get_customers_dict(self) -> dict:
        return {key: value.to_dict() for key, value in self.customers.items()}

    def get_orders_dict(self) -> dict:
        return {key: value.to_dict() for key, value in self.orders.items()}

    def generate_report(self):
        return {'customers': self.get_customers_dict(), 'orders': self.get_orders_dict()}

    def generate_report_ai(self):
        customer_data = "\n".join([
            f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.mail}, Phone: {customer.phone}"
            for customer in self.customers.values()])
        order_data = "\n".join([
            f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Product: {order.product}, Quantity: {order.quantity}, Price: {order.price}, Status: {order.status}"
            for order in self.orders.values()])
        question = f"Generate a sales report based on the following customer and order data:\n\nCustomers:\n{customer_data}\n\nOrders:\n{order_data}. Data must be in format json with keys 'customer', 'order', 'report'."
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a sales manager and you are here to generate a sales report based on customer and order data. You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": question}
        ])
        report = completion.choices[0].message.content
        # report = 
        return report
    
    def save_to_file(self, path, with_ai=False):
        logging.info('start generating report')
        if with_ai:
            data = self.generate_report_ai()
        else:
            data = self.generate_report()
        try:
            with open(path, 'w', encoding="utf-8") as file:
                logging.debug('saving file %s', path)
                json.dump(data, file)
        except Exception as e:
            logging.error(f'Error: {e} in writing file')

def generate_fake_data(manager: Manager, customer_quantity=5, order_quantity=10):
    for _ in range(customer_quantity):
        customer = Customer(fake.uuid4(), fake.name(), fake.email(), fake.phone_number())
        manager.add_customer(customer)

    for _ in range(order_quantity):
        order = Order(fake.uuid4(), fake.random_element(manager.customers.keys()), fake.word(), fake.random_digit(), fake.pricetag())
        manager.create_order(order)

if __name__ == '__main__':
    
    manager = Manager()
    generate_fake_data(manager)
    # customer1 = Customer(fake.uuid4(), fake.name(), fake.email(), fake.phone_number())
    # manager.add_customer(customer1)
    # pprint(manager.generate_report())

    # order1 = Order(fake.uuid4(),customer1.customer_id, fake.word(), fake.random_digit(), fake.pricetag())
    # manager.create_order(order1)
    # pprint(manager.generate_report())

    # manager.update_order(order1.order_id, status='sucsess')
    # pprint(manager.generate_report())

    # print(api_key)
    
    # print(manager.generate_report_ai())
    
    file_path = Path('report.json')
    manager.save_to_file(file_path)
