#---------------------------------------------------------------------------------------------------
# It is a online shop which has some products and some regular customers.
# Also there are some functions which can help a accountant to calculate effortlessly.
#---------------------------------------------------------------------------------------------------

class Product:
    def __init__(self,pName,bPrice,sPrice,pGroup):
        self.pName=pName
        self.bPrice=bPrice
        self.sPrice=sPrice
        self.pGroup=pGroup

    def __str__(self):
        return f"Name: {self.pName}\tBuy Price: ${self.bPrice}\tSell Price: ${self.sPrice}\tGroup Name:{self.pGroup}"
# -----------------------------------------------------------------------------------------------
class Customer:
    def __init__(self,fname,lname,age,city):
        self.fname=fname.capitalize()
        self.lname=lname.capitalize()
        self.age=str(age)
        self.city=city.capitalize()

    def __str__(self):
        return f"First Name :{self.fname}\tLast Name :{self.lname}\tAge :{self.age}\tCity :{self.city}"
# -----------------------------------------------------------------------------------------------
class Shop:
    def __init__(self,shopName):
        self.shopName=shopName
        self.productList=[]
        self.customerList=[]

    def addProduct(self,p):
        self.productList.append(p)

    def addCustomer(self,c):
        self.customerList.append(c)

    def showListOfProducts(self):
        for p in self.productList:
            print(p)

    def showListOfCustomer(self):
        for c in self.customerList:
            print(c)
        
    def showListofbPrice(self):
        for p in self.productList:
            print(p.pName,p.bPrice)      
    
    
    def showListofsPrice(self):
        for p in self.productList:
            print(p.pName,p.sPrice)      


    def showList(self):
        for p in self.productList:
            print(f"Name: {p.pName}\tBuy Price: ${p.bPrice}\tSell Price: ${p.sPrice}\tProfit: ${(p.sPrice) - (p.bPrice)}") 


    def TotalProfit(self):
        sum=0
        for p in self.productList:  
             sum+= p.sPrice-p.bPrice
        print(f"Total profit: {sum}")
#-----------------------------------------------------------------------------------------------------------
# Making instances: 
#-----------------------------------------------------------------------------------------------------------

shop=Shop("TeslaShop")

p01=Product("Apple iPhone 14     ",899,999,"Cell Phones")
p02=Product("Apple iPhone 14 plus",999,1199,"Cell Phones")
p03=Product("Apple iPhone 13     ",699,799,"Cell Phones")
p04=Product("Apple iPhone 13 plus",899,1099,"Cell Phones")
p05=Product("Apple iPhone 12 plus",799,999,"Cell Phones")
p06=Product("Surface laptop 4    ",790,950,"PC")
p07=Product("Surface laptop 4    ",850,1000,"PC")
p08=Product("Surface laptop 4    ",1000,1250,"PC")
p09=Product("Surface laptop 5    ",1000,1350,"PC")
p10=Product("Surface laptop 5    ",1200,1670,"PC")
p11=Product("Surface laptop 5    ",1530,2200,"PC")

c1=Customer("Soheil","Daliri"    ,31,"Tehran")
c2=Customer("Omid"  ,"Hashemi"   ,32,"Tehran")
c3=Customer("Najmeh","Hashemi"   ,34,"Tehran")
c4=Customer("ali   ","Halajzadeh",38,"Tehran")
c5=Customer("Negin" ,"Sarlak"    ,26,"London")

# fname=input("enter name :")
# lname=input("enter family :")
# age=input("enter address :")
# city=input("enter tel :")
# c6=Customer(fname,lname,age,city)

products_dict=[p01.__dict__,p02.__dict__,p03.__dict__,p04.__dict__,p05.__dict__,p06.__dict__,p07.__dict__,
p08.__dict__,p09.__dict__,p10.__dict__,p11.__dict__]

customers_dict=[c1.__dict__,c2.__dict__,c3.__dict__,c4.__dict__,c5.__dict__]

#-----------------------------------------------------------------------------------------------------------
# Running Codes: 
#-----------------------------------------------------------------------------------------------------------
import json


shop.addProduct(p01)
shop.addProduct(p02)
shop.addProduct(p03)
shop.addProduct(p04)
shop.addProduct(p05)
shop.addProduct(p06)
shop.addProduct(p07)
shop.addProduct(p08)
shop.addProduct(p09)
shop.addProduct(p10)
shop.addProduct(p11)

shop.addCustomer(c1)
shop.addCustomer(c2)
shop.addCustomer(c3)
shop.addCustomer(c4)
shop.addCustomer(c5)



# shop.showListOfProducts()
# shop.showListOfCustomer()
# shop.showListofbPrice()
# shop.showListofsPrice()
# shop.showList()
# shop.TotalProfit()



try:
    with open("JsonFiles/online_shop_products.json","w") as shop_products:
            json.dump(products_dict,shop_products,indent=4)
except RuntimeError:
    raise RuntimeError("oops!!!\nsth went wrong in terms of products")
except FileNotFoundError:
    print("There is not a file as the input address")


try:
    with open("JsonFiles/online_shop_customers.json","w") as shop_customers:
        json.dump(customers_dict,shop_customers,indent=4)
    
except RuntimeError:
    raise RuntimeError("oops!!!\nsth went wrong in terms of customers")
except FileNotFoundError:
    print("There is not a file as the input address")
