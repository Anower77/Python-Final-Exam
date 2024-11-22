from bank import Bank

def admin_menu(bank):
    while True:
        print("\n Admin Menu")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. List All user")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loans")
        print("6. Loan Feature")
        print("7. Logout")

        admin_choice = input("Enter your choice: ")

        if admin_choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_number = bank.create_user_account(name, email, address)
            print(f"Accoutnt created successfully! Account Number: {account_number}")                  
        
        elif admin_choice == "2":
            acc_no = int(input("Enter account number to delete: "))
            print(bank.delete_user_account(acc_no))
        
        elif admin_choice == "3":
            user_list = bank.list_of_user()
            if user_list:
                for user in user_list:
                    print(user)
                else:
                    print("No users found!")

        elif admin_choice == "4":
            print(bank.cheak_total_balance())
        
        elif admin_choice == "5":
            print(bank.cheak_total_loans())
        
        elif admin_choice == "6":
            print(bank.loan_feature())
        
        elif admin_choice == "7":
            break
        
        else:
            print("Invalid choice, Try again.")