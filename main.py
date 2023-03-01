# This is the main menu

def menu():
    print("Welcome to our service!! Choose Option")
    print("1. Customer operations")
    print("2. Product operations")
    print("3. Queries")
    print("4. Exit")


menu()

loop = 1
while loop == 1:
    choice = int(input("Select option: "))
    choice = int(choice)
    if choice == 1:
        customer_operations()
        menu()
        pass
    elif choice == 2:
        product_operation()

        menu()
        pass
    elif choice == 3:
        queries()

        menu()
        pass
    elif choice == 4:
        loop = 0

    else:
        print("Please enter 1, 2, 3 or 4")
        menu()


# Customer product system used by customer to make purchases

def main():
    menu()
