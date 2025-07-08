bal = 10000
pin = 5588

print("Welcome to canara bank ATM")
print("Insert your card(yes/no?)")
insert_card = input()
if insert_card.lower() == "yes":
    print("Enter your 4 digit pin:")
    entered_pin = int(input())
    
    if (entered_pin == pin):
        print("SELECT YOUR LANGUAGE")
        print("1. English")
        print("2. kannada")
        print("3. Hindi")
        language = int(input("Enter your choice: "))
        
        if (language == 1):
            print("SELECT YOUR OPTION")
            print("1. Cash Withdrawal")
            print("2. cash deposit")
            print("3. Balance Enquiry")

            option = int(input("Enter your choice: "))
            if (option == 1):
                print("Enter the amount to withdraw:")
                amount = int(input())
                if (amount <= bal):
                    bal = bal - amount
                    print("please wait, your transaction is processing.......")
                    print("Please collect your cash")

                    print("Do you want to check your balance? (yes/no)")
                    checkBalance = input()
                    if (checkBalance.lower() == "yes"):
                        print("Your current balance is:", bal)
                else:
                    print("Insufficient balance!")
            
            elif (option == 2):
                print("Enter the amount you want to deposit:")
                print("Please insert your cash into the deposit slot.")
                deposit_amount = int(input())
                bal = bal + deposit_amount
                print("Please wait, your transaction is processing.......")
                print("Your amount has been deposited successfully.")
                
                print("Do you want to check your balance? (yes/no)")
                checkBalance = input()
                if (checkBalance.lower() == "yes"):
                    print("Your available balance is:", bal)
                           

            elif (option == 3):
                print("Your available balance is:", bal)

            else:
                print("Invalid option selected. Please try again.")

        print("Thank you, visit again!")

    else:
        print("Incorrect pin. Please try again.")







