# This calculator can perform four main operations

# def cal():

#     c1=input("Enter one of the four main operation (+ - * /): ")
#     c2=float(input("Enter a number: "))
#     c3=float(input("Enter a number: "))

#     if c1 == "+" or c1 == "-" or c1 == "*" or c1 == "/":
        
#         if c1 == "+":
#             return f"Result of the operation is: {c2+c3}"
#         elif c1 == "-":
#             return f"Result of the operation is: {c2-c3}"
#         elif c1 == "*":
#             return f"Result of the operation is: {c2*c3}"
#         elif c1 == "/":
#             return f"Result of the operation is: {c2/c3}"

#     else:
#         print("oops!!!\nEnter a correct form of operation")  


#second procedure


def sum(num1,num2):
    return num1+num2 

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def cal():
    
    c1=eval(input("Enter one of the four main operation (sum, sub, mul, div): "))
    c2=float(input("Enter a number: "))
    c3=float(input("Enter a number: "))

    return c1(c2,c3)

#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

a=cal()
print(a)



