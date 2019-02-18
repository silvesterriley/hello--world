class person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def my_results(self):
        print("i am called {0} and my age is {1}".format(self.name,self.age))
p1=person("samantha", 50)
p2=person("judy",40)

p1.my_results()

p2.my_results()

class account(object):
    def __init__(self,name,account_number,initial_amount):
        self.name=name
        self.no=account_number
        self.balance=initial_amount
    
    
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        self.balance-=amount

    def dump(self):
        s= "%s %s ,balance :%s" %(self.name,self.no,self.balance)
        print (s)



customer1=account("bridge",56090,20000)

customer1.deposit(1500)
customer1.withdraw(1000)

customer1.dump()

        
        