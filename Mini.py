d = {}


def add_customer():
    cust_id = input("enter the id number")
    cust_name = input("enter the customer name")
    cust_num = input("enter the customer number")
    cust_init = int(input("enter the initial amount"))
    d.update({cust_id: [cust_name, cust_num, cust_init]})


def payment():
    cust_id = input("enter the id number of the customer")
    for i in d:
        if(i == ust_id):
            n = int(input("1.Consumer pay\n2.Consumer Credit"))
            if(n == 1):
                upd_amt = int(input("Enter the amount"))
                d[cust_id][2] = d[cust_id][2] - upd_amt
            elif(n == 2):
                upd_amt = int(input("Enter the amount"))
                d[cust_id][2] = d[cust_id][2] + upd_amt
            else:
                print("Enter a valid input")
                payment()
            return
    print("Customer not found")


def edit_customer():
    cust_id = input("enter the id number of the customer")
    for i in d:
        if(i == cust_id):
            n = int(input("1.Change Name\n2.Change Number"))
            if(n == 1):
                upd_name = input("Enter the new name")
                d[cust_id][0] = upd_name
            elif(n == 2):
                upd_num = input("Enter the new number")
                d[cust_id][1] = upd_num
            else:
                print("Enter a valid input")
                edit_customer()
            return
    print("Customer not found")


def view_all():
    n = 0
    for i in d:
        n = n + 1
        print("Customer Id: " + i)
        print("Customer Name: " + d[i][0])
        print("Customer Number: " + d[i][1])
        print("Amount to be paid: " + str(d[i][2]))
        print("\n")
    if(n == 0):
        print("No customers found")


print(" Deepak's Grocery Stores Customer Accounting System")
print("1.Add a customer\n")
print("2.Payment by Customer\n")
print("3.Edit customer details\n")
print("4.View all customers")

while(1):
    n = int(input())
    if(n == 1):
        add_customer()
    elif(n == 2):
        payment()
    elif(n == 3):
        edit_customer()
    elif(n == 4):
        view_all()
    else:
        print("Enter a valid input")
        continue
    t = input("Do you wish to continue ? (Y / N)")
    if(t == "N"):
        print(" Deepak's Grocery Stores Customer Accounting System")
        break
    elif(t == "Y"):
        print("1.Add a customer\n")
        print("2.Payment by Customer\n")
        print("3.Edit customer details\n4.View all customers")
        continue
