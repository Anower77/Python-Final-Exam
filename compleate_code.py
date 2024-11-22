import random

class Bank:
    def __init__(self):
        self.user = {}
        self.admin_password = "admin77"
        self.total_balance = 0
        self.total_loan = 0
        self.is_loan = True

    # Random Account Number
    def generate_account_number(self):
        return random.randint(1000000, 9999999)
    

    # Admin Menu
    def admin_login(self, password):
        return password == self.admin_password
    


    # 1. Create user account  
    def create_user_account(self, name, email, address):
        account_number = self.generate_account_number()
        self.user[account_number] = {
            "name": name,
            "email": email,
            "address": address,
            "balance": 0,
            "transactions": [],
            "loan_count": 0
        }
        return account_number
    
    
    # 2. Delete user account 
    def delete_user_account(self, account_number):
        if account_number in self.user:
            del self.user[account_number]
            print(f"Account {account_number} deleted successfully...!!")
        else:
            print(f"Account doesn't exist.")
        
    
    # 3. list of user
    def list_of_user(self):
        if not self.user:
            print("There are No user in Bank!")
        else:
            for acc, details in self.user.items():
                print(f"Accout Number: {acc}, Name: {details['name']}, Balance: {details['balance']}")

    
    # 4. Cheak total balance
    def cheak_total_balance(self):
        print(f"Total Balance: {self.total_balance}")
    
    # 5. Cheak total loans
    def cheak_total_loans(self):
        print(f"Total Loan : {self.total_loan}")

    
    # 6. loan feature
    def loan_feature(self):
        if self.is_loan:
            self.is_loan = False
            print(f"Loan feature is Disabled.")
        else:
            self.is_loan = True
            print(f"Loan feature is Enabled.")



    # User Menu 

    # 1. Deposite
    def deposite(self, account_number, amount):
        if account_number in self.user:
            self.user[account_number]["balance"] += amount
            self.total_balance += amount
            self.user[account_number]["transactions"].append(f"Deposited: {amount}")
            print("Deposite successful!")
        else:
            print(f"Account doesn't exist.")


    # 2. Withdraw 
    def withdraw(self, account_number, w_amount): 
        if account_number in self.user:
            if self.user[account_number]["balance"] >= w_amount:
                self.user[account_number]["balance"] -= w_amount
                self.total_balance -= w_amount
                self.user[account_number]["transactions"].append(f"Withdrew: {w_amount}")
                print("Withdrawal successful!")
            else:
                print("Withdrawal amount exceded.")
        else:
            print("Account doesn't exist.")
            

    # 3. Check balance 
    def check_balance(self, account_number):
        if account_number in self.user:
            print(f"Available Balance: {self.user[account_number]['balance']}")
        else:
            print("Account doesn't exist.")


    # 4. Transaction history
    def transaction_history(self, account_number):
        if account_number in self.user:
            print("Transaction History: ")
            for transaction in self.user[account_number]["transactions"]:
                print(transaction)
        else:
            print("Account doesn't exist.")


    # 5. Take loan
    def take_loan(self, account_number, amount):
        if account_number in self.user:
            if self.is_loan:
                if self.user[account_number]["loan_count"] < 2:
                    self.user[account_number]["balance"] += amount
                    self.total_loan += amount
                    self.user[account_number]["loan_count"] += 1
                    self.total_balance += amount
                    self.user[account_number]["transactions"].append(f"Loan Taken: {amount}")
                    print("Transaction successful! ypu got the loan")
                else:
                    print("Loan limit exceeded.")
            else:
                print("Loan feature is disabled.")
        else: 
            print("Account doesn't exist.")






    # 6. Transfer
    def transfer(self, from_account, to_account, amount):
        if from_account in self.user and to_account in self.user:
            if self.user[from_account]["balance"] >= amount:
                self.user[from_account]["balance"] -= amount
                self.user[to_account]["balance"] += amount
                self.user[from_account]["transactions"].append(f"Transferred {amount}) to {to_account}")
                self.user[to_account]["transactions"].append(f"Received {amount} from {from_account}")
                print("Transfer successful!")
            else:
                print("Yon haven't enought amount")
        else:
            print("Account doesn't exist.")


    # 7. check Bankruptcy
    def check_bankruptcy(self, account_number):
        if account_number in self.user:
            if self.user[account_number]["balance"] == 0:
                print("Bank is bankrupt")
            else:
                print("Bank is Stable")
        else:
            print("Account doesn't exist.")








# Main function
def main():
    bank = Bank()

    while True:
        print("\n Banking Management System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1": # All Admin choice
            password = input("Enter admin password: ")
            if bank.admin_login(password):
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
                        bank.delete_user_account(acc_no)
                    elif admin_choice == "3":
                        bank.list_of_user()
                    elif admin_choice == "4":
                        bank.cheak_total_balance()
                    elif admin_choice == "5":
                        bank.cheak_total_loans()
                    elif admin_choice == "6":
                        bank.loan_feature()
                    elif admin_choice == "7":
                        break
                    else:
                        print("Invalid choice, Try again.")
            else:
                print("Incorrect password!")


        elif choice == "2": # All User Choice
            acc_no = int(input("Enter your account number: "))
            if acc_no in bank.user:
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
                        bank.deposite(acc_no, amount)
                    elif user_choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        bank.withdraw(acc_no, amount)
                    elif user_choice == "3":
                        bank.check_balance(acc_no)
                    elif user_choice == "4":
                        bank.transaction_history(acc_no)
                    elif user_choice == "5":
                        amount = float(input("Enter loan amount: "))
                        bank.take_loan(acc_no, amount)
                    elif user_choice == "6":
                        to_account = int(input("Enter account number who is recive it: "))
                        amount = float(input("Enter transfer amount: "))
                        bank.transfer(acc_no, to_account, amount)
                    elif user_choice == "7":
                        bank.check_bankruptcy(acc_no)
                    elif user_choice == "8":
                        break
                    else:
                        print("Invalid choice, Try again.")
            else:
                print("Account doesn't exist.")


        elif choice == "3":
            print("Exiting system....!!!!!")
            break
        else:
            print("invalid choice, Try again..")


if __name__ == "__main__":
    main()