"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self, first_name, last_name, email, password):
        """Initializes a customer with first and last name, and email and password"""
        
        self.customer_id = 0
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {} {} {}>".format(
            self.first_name, self.last_name, self.email)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {id: Customer object}
    """

    customers = {}
    customer_counter = 0

    for line in open(filepath):
        first_name, last_name, email, password = line.strip().split("|")
        customer_counter += 1
        customer_id = customer_counter

        customers[customer_id] = Customer(first_name,
                                          last_name,
                                          email,
                                          password)


    return customers
