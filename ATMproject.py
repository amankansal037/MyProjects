import time


print("Please insert your card...")
x = 5
while x!=0:
    print(f'"We are reading your card\n Please wait untill {x} seconds"')
    time.sleep(1)
    x -=1
password = 1234
try:
    pin = int(input("Enter ATM pin: "))
except ValueError:
    print("Enter PIN in numbers correctly and Try again.")
balance = 5000

if pin == password:
    print(
        "What you want to do today? \n"
        "Press\n"
        "1 == balance\n"
        "2 == withdraw balance\n"
        "3 == Deposit Balance\n"
        "4 == Exit\n"
    )
    try:
        option = int(input("Please enter your choice: "))
        if option == 1:
            print("Your current balance is", balance)
        elif option== 2:
            print("How much withdaw amount? ")
            withdraw = int(input("Enter the amount: "))
            while withdraw>0:
                if balance >= withdraw:
                    balance -= withdraw
                else:
                    print("You cannot withdraw more than your balance.")
            else:
                print("You cannot withdraw in negative.")
            print(f"Your current balance left is {balance}")
        elif option == 3:
            deposit = int(input("Enter the amount: "))
            while deposit>0:
                balance += deposit
            else:
                print("You cannot deposit in negative. Try again.")
            print(f"Your current balance now is {balance}")
        elif option == 4:
            print("Have a good day...!")
            exit()
#        else:
#            print("Enter the valud command and Try Again.")
    except:
        print("Please enter valid value.")
    pass
else:
    print("Wrong PIN, Try again")
