class Customer:
    id_counter = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id_counter
        Customer.id_counter += 1

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'

    @staticmethod
    def get_next_id():
        if Customer.id_counter == 1:
            return 1
        return Customer.id_counter
