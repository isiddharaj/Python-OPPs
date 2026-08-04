#Create a BankAccount class with account holder name and balance. Display account details.

class BankAccount:
    def __init__(self,Accholder_name):
        self.Accholder_name=Accholder_name
        self.balance=50000

    def account_details(self):
        print("Account holder Name: ",self.Accholder_name)
        print("Account Balance: ",self.balance)

b=BankAccount("Shyam")
b.account_details()