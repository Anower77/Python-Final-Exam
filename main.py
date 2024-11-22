from bank import Bank
from admin import admin_menu
from user import user_menu

def main():
    bank = Bank()

    while True:
        print("\n Banking Management System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
    
        if choice == "1": #admin login
            password = input("Enter admin password: ")
            if bank.admin_login(password):
                admin_menu(bank)
            else:
                print("Incorrect password!")
        
        elif choice == "2": #user login
            account_number = int(input("Enter your account number: "))
            if account_number in bank.user:
                user_menu(bank, account_number)
            else:
                print("Account doesn't exist.")
        
        elif choice == "3":
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
