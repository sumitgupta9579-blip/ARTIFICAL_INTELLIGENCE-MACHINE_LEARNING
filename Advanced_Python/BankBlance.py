class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit_account(self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount
        else:
            print("Insufficient balance")
    def showbalance(self):
        print(self.balance)

c1=BankAccount("Sumit",10000)


c1.showbalance()
c1.deposit_account(5000)
c1.showbalance()
c1.withdraw(9000)
c1.showbalance()


