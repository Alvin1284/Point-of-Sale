import os

PRODUCTS = []


# Product class
class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return "Id:" + str(self.customer_id) + \
                ", Name:" + self.name + \
                ", Quantity:" + str(self.quantity) + \
                ", Price:" + str(self.price)


# Product operations menu
def product_operation():
    # Product menu
    print("Welcome to Product operations")
    loop = 1
    while loop == 1:
        product_op = int(input("Choose your operation:\n"
                               "1) List product\n"
                               "2) List all products\n"
                               "3) Insert a new product\n"
                               "4) Delete a product\n"
                               "5) Update product data\n"
                               "6) Exit\n"))
        if product_op == 1:
            list_product()
        elif product_op == 2:
            all_products()
        elif product_op == 3:
            insert_product()
            print(PRODUCTS)
        elif product_op == 4:
            delete_product()
        elif product_op == 5:
            update_product()
        elif product_op == 6:
            loop = 0
        else:
            print("Wrong input")
            product_operation()


# Functions for product operations
def insert_product():
    with open("ProductData.txt", "r") as file1:

        # Check for similar id
        product_id = input("Enter Product id: ")
        id_list = []
        lines = file1.readlines()
        for line in lines:
            s = line.strip()
            li = s.split("~")
            id_list.append(li[0])

            if product_id in id_list:
                print("Product already exists,please enter another Product id")
                return insert_product()

    product_name = input("Enter Product name: ")
    product_quantity = input("Enter Product Quantity: ")
    product_price = input("Enter Product price: ")
    data = Product(product_id, product_name, product_quantity, product_price)
    PRODUCTS.append(data)
    # write customer to file
    with open('ProductData.txt', 'a+', newline='') as file:
        for product in PRODUCTS:
            file.write(product.id + "~" + product.name + "~" + product.quantity + "~" + product.price + '\n')


# Delete Product
def delete_product():
    with open("ProductData.txt", "r+") as file2:
        product_id = input("Enter product id to delete: ")
        lines = file2.readlines()
        file2.seek(0)
        for line in lines:
            if not product_id in line.split("~")[0]:
                file2.write(line)
        file2.truncate()
        print("Product Deleted Successfully!!")


def update_product():
    file = open("ProductData.txt", "r")
    file1 = open("temp1.txt", "w")
    product_id = int(input("Enter Product id to update:"))

    s = ' '
    while s:
        s = file.readline()
        li = s.split("~")
        if len(s) > 0:
            if int(li[0]) == product_id:
                product_id = input("Enter Product id:")
                product_name = input("Enter Product name:")
                product_amount = input("Enter Product Amount:")
                product_price = input("Enter Product Price:")
                file1.write(product_id + "~" + product_name + "~" + product_amount + "~" + product_price + "\n")
            else:
                file1.write(s)
    file.close()
    file1.close()
    os.remove("ProductData.txt")
    os.rename("temp1.txt", "ProductData.txt")


def list_product():
    file = open("ProductData.txt", "r")
    product_id = int(input("Enter product id: "))

    s = ' '

    while s:
        s = file.readline()
        li = s.split("~")
        if len(s) > 0:
            if int(li[0]) == product_id:
                print("Product id:", li[0])
                print("Product Name:", li[1])
                print("Product Amount:", li[2])
                print("Product Price:", li[3])


def all_products():
    file = open("ProductData.txt", "r")

    s = file.readlines()

    print(s)


def fill_products():
    file = open("ProductData.txt", "r")
    for i in file:
        prod = i.split("~")
        id = prod[0]
        name = prod[1]
        quantity = prod[2]
        price = prod[3]
        output = Product(id, name, quantity, price)
        PRODUCTS.append(output)