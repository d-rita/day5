class BankAccount:
    balance=0
    def __init__(self, name):
        self.name=name
        
    def get_balance(self):
        if self.balance==None:
            raise ValueError
        else:
            return self.balance

    def open(self):
        self.get_balance()


    def deposit(self, amount):
        if self.balance==None:
            raise ValueError
        else:
            if amount<0:
                raise ValueError
            elif amount== 0:
                raise ValueError
            else:
                self.balance+=amount
                self.get_balance()

    def withdraw(self, amount):
        if self.balance==None:
            raise ValueError
        else:
            if amount>self.balance:
                raise ValueError
            elif amount<0:
                raise ValueError
            else:
                self.balance-=amount
                self.get_balance()

    def close(self):
        self.name=None
        self.balance=None
        
