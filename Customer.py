import os

CUSTOMERS = []


# Customer class
class Customers:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def __str__(self):
        return "Id:" + str(self.id) + \
            ", Name:" + self.name + \
            ", Address:" + str(self.address)


def customer_operations():
    # Customer operations menu
    print("Welcome to Customer Operations")
    loop = 1
    while loop == 1:
        operations = int(input("Select operations:\n "
                               "1) List Customers\n"
                               "2) List all Customers\n"
                               "3) Insert customer\n"
                               "4) Delete customer\n"
                               "5) Update customer\n"
                               "6) Exit\n"))

        if operations == 1:
            list_customer()
        elif operations == 2:
            all_customers()
        elif operations == 3:
            insert_customer()
            print(CUSTOMERS)
        elif operations == 4:
            delete_customer()
        elif operations == 5:
            update_customer()
        elif operations == 6:
            loop = 0
        else:
            print("Wrong input")
            customer_operations()


# Creating and storing Customers in list


def insert_customer():
    with open("CustomerData.txt", "r") as file1:
        customer_id = input("Enter Customer id: ")
        id_list = []
        lines = file1.readlines()
        for line in lines:
            s = line.strip()
            li = s.split("~")
            id_list.append(li[0])

            if customer_id in id_list:
                print("Customer already exists,please enter another Customer id")
                return insert_customer()

        customer_name = input("Enter Customer name: ")
        customer_address = input("Enter address: ")
        data = Customers(customer_id, customer_name, customer_address)
        CUSTOMERS.append(data)
        # write customer to file
        with open('CustomerData.txt', 'a+', newline='') as file:
            for customer in CUSTOMERS:
                file.write(customer.id + "~" + customer.name + "~" + customer.address + '\n')


def delete_customer():
    with open("CustomerData.txt", "r+") as file2:
        customer_id = input("Enter Customer id to delete: ")
        lines = file2.readlines()
        file2.seek(0)
        for line in lines:
            if not customer_id in line.split("~")[0]:
                file2.write(line)
        file2.truncate()
        print("Customer Deleted Successfully!!")


def update_customer():
    file = open("CustomerData.txt", "r")
    file1 = open("temp.txt", "w")
    customer_id = int(input("Enter Customer id to update:"))

    s = ' '
    while s:
        s = file.readline()
        li = s.split("~")
        if len(s) > 0:
            if int(li[0]) == customer_id:
                customer_id = input("Enter Customer id:")
                customer_name = input("Enter Customer name:")
                customer_address = input("Enter Customer address:")
                file1.write(customer_id + "~" + customer_name + "~" + customer_address + "\n")
            else:
                file1.write(s)
    file.close()
    file1.close()
    os.remove("CustomerData.txt")
    os.rename("temp.txt", "CustomerData.txt")


def list_customer():
    file = open("CustomerData.txt", "r")
    customer_id = input("Enter Customer id: ")

    s = ' '

    while s:
        s = file.readline()
        li = s.split("~")
        if len(s) > 0:
            if li[0] == customer_id:
                print("Customer id:", li[0])
                print("Customer Name:", li[1])
                print("Customer Address:", li[2])


def all_customers():
    file = open("CustomerData.txt", "r")

    s = file.readlines()

    print(s)
