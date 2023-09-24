# static attribute (class attribute)
# sattic method @staticmethod
#class method @classmethod



class Shopping:
    cart = [] #class attribute #static attribute
    origin = 'china'

    def __init__(self,name,location) -> None:
        self.name = 'jamuna city'  #instance
        self.location = 'Basundhara'

    def purchase(self,item,price,amount):
        remaining = amount - price
        
        print(f'buying: {item} for price:{price} and remaining:{remaining}')

    @classmethod
    
    def hudai_dekhi(self,item):
        print('hudai dekhi kintu kinbo na just ac er hawa khaite ashchi',item)

#Shopping.purchase()
basundhara = Shopping('basundh arate' 'not popular')
#basundhara.purchase('lungi',500,1000)
Shopping.hudai_dekhi('lungi')



#static e instance use kora jabe na