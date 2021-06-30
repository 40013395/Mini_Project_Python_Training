"""
Name: Grocery Store Accounts Management
Author: Deepak
Date: 24/05/2020
"""


d = []


class Customer:
    """Summary or Description of the class

        Parameters:
        None

        Returns:
        None

        Operation:
        Adds customer to database and performs required operations on customer's account
    """
    def __init__(self, id_num, name, num, init):
        self.customer_id = id_num
        self.customer_name = name
        self.customer_num = num
        self.customer_init = init

    def payment(self, amt, input_option):
        """Summary or Description of the Function

            Parameters:
            None

            Returns:
            None

            Operation:
            Payment related operations
        """
        if input_option == 1:
            self.customer_init = self.customer_init - amt
        elif input_option == 2:
            self.customer_init = self.customer_init + amt

    def edit_customer(self, input_option):
        """Summary or Description of the Function

            Parameters:
            None

            Returns:
            None

            Operation:
            Edit customer details
        """
        if input_option == 1:
            upd_name = input("Enter the new name")
            self.customer_name = upd_name
        elif input_option == 2:
            upd_num = input("Enter the new number")
            self.customer_num = upd_num


class LoyalCustomer(Customer):
    """Summary or Description of the class

            Parameters:
            None

            Returns:
            None

            Operation:
            Subclass of customer with a 'Loyalty' tag
        """
    def bonus(self, amount):
        """Summary or Description of the class

            Parameters:
            None

            Returns:
            None

            Operation:
            adds bonus for loyal customers
        """
        self.customer_init = self.customer_init - amount


class LateCustomer(Customer):
    """Summary or Description of the class

            Parameters:
            None

            Returns:
            None

            Operation:
            Subclass of customer with a 'Late' tag
        """
    def penalty(self, amount):
        """Summary or Description of the class

            Parameters:
            None

            Returns:
            None

            Operation:
            adds penalty for late customers
        """
        self.customer_init = self.customer_init + amount


if __name__ == "__main__":
    while 1:
        print(" Deepak's Grocery Stores Customer Accounting System")
        print("1.Add a customer")
        print("2.Payment by Customer")
        print("3.Edit customer details")
        print("4.View all customers")
        choice = int(input())
        if choice == 1:
            option = int(input("1. Regular\n2. Loyal\n3. Late\n"))
            customer_id = input("enter the id number: ")
            customer_name = input("enter the customer name: ")
            customer_num = input("enter the customer number: ")
            customer_init = int(input("enter the initial amount: "))
            if option == 1:
                c = Customer(customer_id, customer_name, customer_num, customer_init)
            elif option == 2:
                c = LoyalCustomer(customer_id, customer_name, customer_num, customer_init)
                c.bonus(500)
            else:
                c = LateCustomer(customer_id, customer_name, customer_num, customer_init)
                c.penalty(500)
            d.append(c)
        elif choice == 2:
            ci = input("enter the id number of the customer: ")
            CC = 0
            for i in d:
                if i.customer_id == ci:
                    CC = CC + 1
                    while 1:
                        x = int(input("1.Consumer pay\n2.Consumer Credit\n"))
                        if x in (1, 2):
                            upd_amt = int(input("Enter the amount: "))
                            i.payment(upd_amt, x)
                            break
                        print("Enter a valid option")
            if CC == 0:
                print("No customers found")
        elif choice == 3:
            ci = input("enter the id number of the customer: ")
            CC = 0
            for i in d:
                if i.customer_id == ci:
                    CC = CC + 1
                    while 1:
                        x = int(input("1.Change Name\n2.Change Number\n"))
                        if x in (1, 2):
                            i.edit_customer(x)
                            break
                        print("Enter a valid option")
            if CC == 0:
                print("No customers found")
        elif choice == 4:
            CC = 0
            for i in d:
                CC = CC + 1
                print("Customer Id: " + i.customer_id)
                print("Customer Name: " + i.customer_name)
                print("Customer Number: " + i.customer_num)
                print("Amount to be paid: " + str(i.customer_init))
                print("\n")
            if CC == 0:
                print("No customers found")
        else:
            print("Enter a valid input")
            continue
        proceed_option = input("Do you wish to continue ? (Y / N): ")
        if proceed_option != "Y":
            print(" Thank you ")
            break
