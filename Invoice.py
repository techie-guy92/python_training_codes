class Product:

    def __init__(self,productCode,productName,price,productGroupName):
        self.productCode= productCode
        self.productName= productName
        self.price= price
        self.productGroupName=productGroupName
        
    def __str__(self):
        return f"{self.productCode}\t{self.productName}\t{self.price}\t{self.productGroupName}\t"
#--------------------------------------------------------------------
class Customer:

    def __init__(self,customerCode,name,family,mobile):
        self.customerCode = customerCode
        self.name = name
        self.family = family
        self.mobile = mobile
#-------------------------------------------------------------------
class BillDetails:

    def __init__(self,billDetailCode,billCode,productCode,productCount):
        self.billDetailCode = billDetailCode
        self.billCode = billCode
        self.productCode = productCode
        self.productCount = productCount
        
    def __str__(self):
        return f"{self.billDetailCode}\t{self.billCode}\t{self.productCode}\t{self.productCount}\t"
#-------------------------------------------------------------------
import datetime

class Bill:

    def __init__(self,billCode,customerCode):
        self.billCode = billCode
        self.billDate =str(datetime.datetime.now()) 
        self.customerCode = customerCode
        self.billDetails=[]

    def __str__(self):
        return f"{self.billCode}\t{str(self.billDate)}\t{self.customerCode}\t"
#--------------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------------- 
import json

def readProductFromJsonFile():
    with open("JsonFiles/products.json",'r') as file1:
        products=json.load(file1)
    return products
    
    
def readCustomersFromJsonFile():
    with open("JsonFiles/customers.json",'r') as file1:
        customers=json.load(file1)
    return customers


def showProductList(products):
    for product in products:
        print(product)


def showCustomerList(customers):
    for customer in customers:
        print(customer)



#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------  

products=readProductFromJsonFile()       
showProductList(products)    
print(80*'-')
customers=readCustomersFromJsonFile()       
showCustomerList(customers)     


#-------------------------------------------------------------


def createBill(billCode,customerCode):
    bill1=Bill(billCode,customerCode)
    bt1=BillDetails(1,billCode,1,5)
    bt2=BillDetails(2,billCode,3,10)
    bt3=BillDetails(3,billCode,2,4)
    bill1.billDetails=[bt1.__dict__,bt2.__dict__,bt3.__dict__]
    return bill1.__dict__      



def readBillFromJsonFile():
    with open("JsonFiles/bills.json",'r') as file1:
        try:
            currentBills=json.load(file1)
        except:
            currentBills=[]
    return currentBills

def writeBillsToJsonFile(bills):
    with open("JsonFiles/bills.json",'w') as file1:
        json.dump(bills, file1,indent=4)


currentBills=readBillFromJsonFile()                   #کل فاکتورهای درون فایل
myBill=createBill(1,10000)                              #فاکتور جدید
currentBills.append(myBill)
myBill=createBill(2,10001)                              #فاکتور جدید
currentBills.append(myBill)
myBill=createBill(3,10005)                              #فاکتور جدید
currentBills.append(myBill)
writeBillsToJsonFile(currentBills)
