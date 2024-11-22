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
            return f"Account {account_number} deleted successfully...!!"
        else:
            return f"Account doesn't exist."
        
    
    # 3. list of user
    def list_of_user(self):
        if not self.user:
            return "There are No user in Bank!"
        
        user_list = []
        for account_number, details in self.user.items():
            user_info = f"Account Number: {account_number}, Name: {details['name']}, Balance: {details['balance']}"
            user_list.append(user_info)
        return user_list
    
    # 4. Cheak total balance
    def cheak_total_balance(self):
        return f"Total Balance: {self.total_balance}"
    
    # 5. Cheak total loans
    def cheak_total_loans(self):
        return f"Total Loan : {self.total_loan}"

    
    # 6. loan feature
    def loan_feature(self):
        if self.is_loan:
            self.is_loan = False
            return "Loan feature is Disabled."
        else:
            self.is_loan = True
            return "Loan feature is Enabled."



    # User menu 
    # 1. deposite 
    def deposite(self, account_number, amount):
        if account_number in self.user:
            self.user[account_number]["balance"] += amount
            self.total_balance += amount
            self.user[account_number]["transactions"].append(f"Deposited: {amount}")
            return "Deposit successful!"
        else:
            return "Account doesn't exist."


    # 2. withdraw
    def withdraw(self, account_number, w_amount): 
        if account_number in self.user:
            if self.user[account_number]["balance"] >= w_amount:
                self.user[account_number]["balance"] -= w_amount
                self.total_balance -= w_amount
                self.user[account_number]["transactions"].append(f"Withdrew: {w_amount}")
                return "Withdrawal successful!"
            else:
                return "Withdrawal amount exceeded."
        else:
            return "Account doesn't exist."


    # 3. check balance 
    def check_balance(self, account_number):
        if account_number in self.user:
            return f"Available Balance: {self.user[account_number]['balance']}"
        else:
            return "Account doesn't exist."

    # 4. transaction history
    def transaction_history(self, account_number):
        if account_number in self.user:
            print("Transaction History: ")
            for transaction in self.user[account_number]["transactions"]:
                print(transaction)
        else:
            return "Account doesn't exist."


    # 5. take loan
    def take_loan(self, account_number, amount):
        if account_number in self.user:
            if self.is_loan:
                if self.user[account_number]["loan_count"] < 2:
                    self.user[account_number]["balance"] += amount
                    self.total_loan += amount
                    self.user[account_number]["loan_count"] += 1
                    self.total_balance += amount
                    self.user[account_number]["transactions"].append(f"Loan Taken: {amount}")
                    return "Loan granted successfully!"
                else:
                    return "Loan limit exceeded."
            else:
                return "Loan feature is disabled."
        else: 
            return "Account doesn't exist."
        

    # 6.transfer
    def transfer(self, from_account, to_account, amount):
        if from_account in self.user and to_account in self.user:
            if self.user[from_account]["balance"] >= amount:
                self.user[from_account]["balance"] -= amount
                self.user[to_account]["balance"] += amount
                self.user[from_account]["transactions"].append(f"Transferred {amount} to {to_account}")
                self.user[to_account]["transactions"].append(f"Received {amount} from {from_account}")
                return "Transfer successful!"
            else:
                return "you haven't enoght amount."
        else:
            return "Account doesn't exist."
 



    # 7. check bankruptcy
    def check_bankruptcy(self, account_number):
        if account_number in self.user:
            if self.user[account_number]["balance"] == 0:
                return "Bank is bankrupt."
            else:
                return "Bank is stable."
        else:
            return "Account doesn't exist."