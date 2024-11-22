from bank import Bank

def user_menu(bank, account_number):
    while True:
        print("\nUser Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Check Bankruptcy Status")
        print("8. Logout")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            amount = float(input("Enter deposite amount: "))
            print(bank.deposite(account_number, amount))
        

        elif user_choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid amount!!")
            else:
                print(bank.withdraw(account_number, amount))
        

        elif user_choice == "3":
            print(bank.check_balance(account_number))
        
        elif user_choice == "4":
            transactions = bank.transaction_history(account_number)
            if transactions:
                print("Transaction History: ")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions available.")
            # bank.transaction_history(account_number)
        
        elif user_choice == "5":
            amount = float(input("Enter loan amount: "))
            if amount <= 0:
                print("Invalid amount!!")
            else:
                print(bank.take_loan(account_number, amount))
        
        elif user_choice == "6":
            to_account = int(input("Enter account number who is recive it: "))
            amount = float(input("Enter transfer amount: "))
            if amount <= 0:
                print("Invalid amount!!")
            else:
                print(bank.transfer(account_number, to_account, amount))
        
        elif user_choice == "7":
            print(bank.check_bankruptcy(account_number))
        
        elif user_choice == "8":
            break
        
        else:
            print("Invalid choice, Try again.")