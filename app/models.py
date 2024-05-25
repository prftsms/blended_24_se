class Customer:
    def __init__(self, customer_id, name, mail, phone) -> None:
        self.customer_id = customer_id
        self.name = name
        self.mail = mail
        self.phone = phone

    def to_dict(self):
        return {'customer_id': self.customer_id,
                'name': self.name,
                'mail': self.mail,
                "phone": self.phone
            }


class Order:
    def __init__(self, order_id, customer_id, product, quantity, price, status='pending') -> None:
        self.order_id = order_id
        self.customer_id = customer_id
        self.product = product
        self.quantity = quantity
        self.price = price
        self.status = status

    def to_dict(self):
        return {'order_id': self.order_id,
                'customer_id': self.customer_id,
                'product': self.product,
                'quantity': self.quantity,
                "price": self.price,
                'status': self.status
            }
