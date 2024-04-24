#magicalprime program

class A:
  def mp(self,n):
    name =int(input("Enter the magicalprime number : "))
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#  neon program

class B(A):
  def neon(self,a):
    a = int(input("Enter the neon number : "))
    if a==0 or a==1 or a==9:
      print("Neon number")
    else:
      print("Not a neon number")    
      
 #   X pattern program

class C(A):
  def x(self,name):
        name =str(input("Enter the name for x pattern : "))
        length = len(name)
        for i in range(length):
            for j in range(length):
                if i==j or i+j==length-1:
                    print(name[i],end=" ")
                else:
                    print(" ",end= " ")
            print()

#   reverse program

class E(B,C):
  def reverse(self,name):
    name =str(input("Enter the name to get reversed : "))
    print(name[::-1])

# banking program

class D(A):
   def banking():
        def withdraw(account, amount):
            if amount > account['balance']:
                print("Insufficient funds!")
            else:
                account['balance'] -= amount
                account['transactions'].append(f"Withdrawal: ₹{amount}")
                print(f"Withdrawal successful. Remaining balance: ₹{account['balance']}")

        def deposit(account, amount):
            account['balance'] += amount
            account['transactions'].append(f"Deposit: ₹{amount}")
            print(f"Deposit successful. Remaining balance: ₹{account['balance']}")

        def get_balance(account):
            return account['balance']

        def get_transaction_history(account):
            return account['transactions']

        # Create an account dictionary
        account = {
            'balance': 1000,
            'transactions': []
        }
        #login
        #using dictionary.
        user={'s':1,'z':2,'a':3}

        uemail=str(input("enter the email"))
        upassword=int(input("enter the password"))
        for i in user :
            if(i == uemail):
                if(user[i] == upassword):
                    print("Login successfull")
                

            # Dictionary to map user choices to functions
                    choices = {
                        '1': deposit,
                        '2': withdraw,
                        '3': get_balance,
                        '4': get_transaction_history
                    }

                    while True:
                        print("\n1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Transaction History")
                        print("5. Exit")

                        choice = input("Enter your choice: ")

                        if choice == '5':
                            print("Exiting program.")
                            break

                        if choice in choices:
                            if choice == '1' or choice == '2':
                                amount = float(input("Enter amount: "))
                                choices[choice](account, amount)
                            else:
                                print(choices[choice](account))
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("Invalid mailid or password")

# object of class E...
obj1=E()
print(obj1.mp(1))
obj1.neon(1)
obj1.x("name")
obj1.reverse("name")
  
# object of class D...
    
obj2=D
obj2.banking()

