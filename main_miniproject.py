"""
Name: Grocery Store Accounts Management
Author: Deepak
Date: 24/05/2020
"""


d = {}


def add_customer():
    """Summary or Description of the Function

        Parameters:
        None

        Returns:
        None

        Operation:
        Adds customer to database
    """
    customer_id = input("enter the id number")
    customer_name = input("enter the customer name")
    customer_num = input("enter the customer number")
    customer_init = int(input("enter the initial amount"))
    d.update({customer_id: [customer_name, customer_num, customer_init]})


def payment():
    """Summary or Description of the Function

            Parameters:
            None

            Returns:
            None

            Operation:
            Operates credits and debits
        """
    customer_id = input("enter the id number of the customer")
    for i in d:
        if i == customer_id:
            payment_option = int(input("1.Consumer pay\n2.Consumer Credit"))
            if payment_option == 1:
                upd_amt = int(input("Enter the amount"))
                d[customer_id][2] = d[customer_id][2] - upd_amt
            elif payment_option == 2:
                upd_amt = int(input("Enter the amount"))
                d[customer_id][2] = d[customer_id][2] + upd_amt
            else:
                print("Enter a valid input")
                payment()
            return
    print("Customer not found")


def edit_customer():
    """Summary or Description of the Function

            Parameters:
            None

            Returns:
            None

            Operation:
            Edits the customer details
        """
    customer_id = input("enter the id number of the customer")
    for i in d:
        if i == customer_id:
            edit_option = int(input("1.Change Name\n2.Change Number"))
            if edit_option == 1:
                upd_name = input("Enter the new name")
                d[customer_id][0] = upd_name
            elif edit_option == 2:
                upd_num = input("Enter the new number")
                d[customer_id][1] = upd_num
            else:
                print("Enter a valid input")
                edit_customer()
            return
    print("Customer not found")


def view_all():
    """Summary or Description of the Function

            Parameters:
            None

            Returns:
            None

            Operation:
            View all customers with their details from the database
        """
    customer_count = 0
    for i in d:
        customer_count = customer_count + 1
        print("Customer Id: " + i)
        print("Customer Name: " + d[i][0])
        print("Customer Number: " + d[i][1])
        print("Amount to be paid: " + str(d[i][2]))
        print("\n")
    if customer_count == 0:
        print("No customers found")


print(" Deepak's Grocery Stores Customer Accounting System")
print("1.Add a customer\n")
print("2.Payment by Customer\n")
print("3.Edit customer details\n")
print("4.View all customers")

while 1:
    input_option = int(input())
    if input_option == 1:
        add_customer()
    elif input_option == 2:
        payment()
    elif input_option == 3:
        edit_customer()
    elif input_option == 4:
        view_all()
    else:
        print("Enter a valid input")
        continue
    t = input("Do you wish to continue ? (Y / N)")
    if t == "N":
        print(" Deepak's Grocery Stores Customer Accounting System")
        break
    if t == "Y":
        print("1.Add a customer\n")
        print("2.Payment by Customer\n")
        print("3.Edit customer details\n4.View all customers")
        continue
