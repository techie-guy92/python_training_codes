class checking_Prime:

    def __init__(self,name):
      self.num=name

    def __str__(self):
        return self.num


    def prime_numbers(self,num):
        my_num=num
        a=0
        for i in range(1,my_num+1):
            if my_num%i == 0:
                a+=1
        if a==2:
            print (my_num,"is a prim number")
        else:
            print (my_num,"is not a prim number")


#-----------------------------------------------------------------------------------------------------------
# Making instence: 
#-----------------------------------------------------------------------------------------------------------

x=checking_Prime("Math")
x.prime_numbers(1)





# Prime Number Function

def prime_numbers():
    num=int(input("Enter a number: "))
    a=0
    for i in range(1,num+1):
        if num%i == 0:
            a+=1
    if a==2:
        return f""""{num}" is a prim number"""
    else:
        return f""""{num}" is not a prim number"""


#-----------------------------------------------------------------------------------------------------------
# Running the code: 
#-----------------------------------------------------------------------------------------------------------

x=prime_numbers()
print(x)
