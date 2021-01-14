

class account:
    
    count=0

    @classmethod

    def  incr_count(cls):

         cls.count+=1


    
    @classmethod

    def get_count(cls):

        return cls.count

    @staticmethod

    def print_Val():

        print("static method in account class")




    def __init__(self,cust_id,name,initial_value=10):

        self.__id=cust_id

        self.__name=name

        self.__balance=initial_value

        account.incr_count()

        


    def get_id(self):

        return self.__id

    def get_name(self):

        return self.__name


    def  get_deposit(self):

        return self.__balance


    def deposit(self,ammount):
        self.__balance=self.__balance+ammount
        return self.__balance

    
    def withdraw(self,ammount):
        if ammount > self.__balance:
            return "insufficiant balance"
        else:
            self.__balance -=ammount
            return self.__balance




class Saving_Account(account):

    def __init__(self,id,name,initial_bal=0):

        super().__init__(id,name,initial_bal)
        
        self.limit=50000

    def withdraw(self,ammount):

        if ammount <self.limit:

            new_bal=super().withdraw(ammount)

            self.limit-=ammount

            return new_bal

        else:

            print("daily limit reached")



# customer1=Saving_Account(101,"asif")

# print(customer1.__dict__)


# print(customer1.deposit(50000))

# print(customer1.withdraw(40000))
# print(customer1.withdraw(40000))

# help(Saving_Account)


class A:
    pass

class B:
    pass

class C(A,B):
    pass






# customer1=account("101","abc")
# customer2=account("102","bcd")
# # print(customer1._account__id)
# # print(customer1.__dict__)

# # print(account.count)

# # account.count +=5
# # print(account.count)

# # print(customer1.count)

# # print(customer2.count)

# # customer1.count=100



# # print(account.count)

# # print(customer1.count)

# # print(customer2.count)


# print(account.get_count())


# account.print_Val()

obj=C()
help(obj)