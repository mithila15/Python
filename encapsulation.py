#encapsulation --> hide details 
# access modifier : public,private,protected

class Bank :
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name= holder_name #public attribute
        self._branch = 'banani 11'    #protected '""
        self.__balance = initial_deposit #private attribute


    def deposit(self,amount):
        self.__balance += amount #private
    
    def get_balance(self):
        return self.__balance


rafsan = Bank('DBBl', 10000)

print(rafsan.holder_name)
rafsan.holder_name = 'mithila'
rafsan.deposit(40000)
print(rafsan.get_balance())
print(rafsan.holder_name)

#print(dir(rafsan))
print(rafsan._Bank__balance)
 