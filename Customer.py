import os

CUSTOMERS = []


# Customer class
class Customers:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def set_id(self, customer_id):
        self.customer_id = customer_id

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def __str__(self):
        return "Id:" + str(self.customer_id) + \
            ", Name:" + self.name + \
            ", Address:" + str(self.address)


# Creating and storing Customers in list

customers = []

n = int(input("How many customers do you want to enter?"))
for i in range(n):
    customer_id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    print()  # print blank line
    customer = Customers(customer_id, name, address)
    customers.append(customer)

# Display customer details
print("Customer details:\n")
for customer in customers:
    print
