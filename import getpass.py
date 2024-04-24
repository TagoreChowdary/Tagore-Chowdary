class BankAccount:
    def _init_(self, initial_balance, username, password):
        self.balance = initial_balance
        self.transactions = []
        self.username = username
        self.password = password

    def withdraw(self):
        amount = int(input("enter the wd amt"))
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")

    def deposit(self):
        amount = int(input("enter the amt"))
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

def create_account():
    username = input("Enter a username: ")
    password = int(input("Enter a password: "))
    initial_balance = int(input("Enter an initial balance: "))
    account = BankAccount(initial_balance, username, password)
    return account

def login():
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    with open("accounts.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == username and data[1] == password:
                return BankAccount(int(data[2]), username, password)
    print("Login failed")
    return None

def save_account(account):
    with open("accounts.txt", "a") as f:
        f.write(f"{account.username},{account.password},{account.balance}\n")

def main():
    print("1. Create account")
    print("2. Login")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        account = create_account()
        save_account(account)
        print("Account created successfully")
    elif choice == 2:
        account = login()
        if account is not None:
            print("Balance:", account.get_balance())
            account.deposit()
            account.withdraw()
            account.withdraw()
            print("Balance:", account.get_balance())
            print("Transaction History:", account.get_transaction_history())
            save_account(account)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()