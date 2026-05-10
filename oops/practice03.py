class Account:
    def __init__(self,acc,bal):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited from your account")
        print("the total ammount in your bank account is:",self.get_balance())


    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited from your account")
        print("the total ammount in your bank account is:",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(1234,10000)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(1000)
acc1.credit(1500)

              