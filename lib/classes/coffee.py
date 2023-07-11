class Coffee:
    def __init__(self, name: str):
        self._name = name
        self._orders = []
        self._customers = set()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Cannot change the name of the coffee")
        self._name = value

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order is not None:
            if not isinstance(new_order, Order):
                raise Exception("New order must be of type 'Order'")
            self._orders.append(new_order)
        return self._orders

    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer is not None:
            if not isinstance(new_customer, Customer):
                raise Exception("New customer must be of type 'Customer'")
            self._customers.add(new_customer)
        return list(self._customers)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        return sum(order.price for order in self._orders) / len(self._orders)
