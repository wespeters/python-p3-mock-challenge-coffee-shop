class Order:
    all = []

    def __init__(self, customer, coffee, price: int):
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value):
        if not 1 <= value <= 10:
            raise Exception("Price must be a number between 1 and 10, inclusive")
        self._price = value

    @property
    def customer(self):
        from classes.customer import Customer
        return self._customer

    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if not isinstance(value, Customer):
            raise Exception("Customer must be of type 'Customer'")
        self._customer = value

    @property
    def coffee(self):
        from classes.coffee import Coffee
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if not isinstance(value, Coffee):
            raise Exception("Coffee must be of type 'Coffee'")
        self._coffee = value
