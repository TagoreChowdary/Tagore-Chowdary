def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")


def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
print("WELCOME")
print("Please insert your card")
pin=1234
upin=int(input("enter your pin"))
if(upin==pin):
    choices = {
        '1': withdraw,
        '2': get_balance,
        '3': get_transaction_history
    }

    while True:
        print("\n1. Withdraw")
        print("2. Check Balance")
        print("3. Transaction History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '4':
            print("Exiting program.")
            break

        if choice in choices:
            if choice == '1':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)
            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")
else:
    print("invalid pin")