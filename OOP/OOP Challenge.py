class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep):
        self.balance+=dep
        print("Deposit Accteped")
        print(self.balance)
    def withdraw(self,wid):
        if wid>self.balance:
            print("Funds Unavailable!")
        else:
            self.balance-=wid
            print("Balance After withdraw ")
            print(self.balance)
    def __str__(self):
        return f"Owner ={self.owner} \n  Balance={self.balance}"
acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(30)
acct1.withdraw(10)
acct1.withdraw(1000)