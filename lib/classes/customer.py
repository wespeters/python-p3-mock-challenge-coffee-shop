class Customer:
    def __init__(self, name: str):
        self._name = name
        self._orders = []
        self._coffees = set()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be of type 'str'")
        if not 1 <= len(value) <= 15:
            raise Exception("Name must be between 1 and 15 characters, inclusive")
        self._name = value

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order is not None:
            if not isinstance(new_order, Order):
                raise Exception("New order must be of type 'Order'")
            self._orders.append(new_order)
        return self._orders

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee is not None:
            if not isinstance(new_coffee, Coffee):
                raise Exception("New coffee must be of type 'Coffee'")
            self._coffees.add(new_coffee)
        return list(self._coffees)

    def create_order(self, coffee, price):
        from classes.order import Order
        return Order(self, coffee, price)
