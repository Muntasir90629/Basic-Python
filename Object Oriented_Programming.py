

# cust id
# name 
# balance


# deposit
# withdraw


class Account:
    def __init__(self,cust_id,name,initial_value=0):

        self.__id=cust_id

        self.__name=name

        self.__balance=initial_value

    def get_balance(self):

        return  self.__balance

    def get_id(self):
        return self.__id

     def get_name(self):
        return self.__name


    def deposit(self,ammount):
        self.__balance=self.__balance+ammount
        return self.balance


    def withdraw(self,ammount):
        if ammount > self.balance:
            return "insufficiant balance"
        else:
            self.balance -=ammount
            return self.balance






customer1=Account("101","ABC")

print(customer1._Account__id)
print(customer1.__dicy__)
# print(customer1)
print(customer1.get_balance())
print(customer1.deposit(5000))
print(customer1.withdraw(2000))


customer2=Account("102","xyz")
# print(customer1)
print(customer2.get_balance())
print(customer2.deposit(300))
print(customer2.withdraw(200))
customer3=Account("103","pqr")
# print(customer1)
customer3.deposit(34000)
customer4=Account("104","pdfr")
customer4.deposits(4000)
# print(customer1.id,customer1.name,customer1.balance)
print(customer1)

l=[customer1,customer2,customer3,customer4]

for obj in l:

    if obj.get_balance()<10000:
        print(obj.get_id(),obj.get_name())
