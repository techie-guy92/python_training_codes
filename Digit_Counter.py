#clients are able to input their numbers then the program can count digit of numbers

def digit_counter(num):
 
 c=0
 while num>0 :
     num//=10
     c+=1
 return c


#second procedure


# def digit_counter(num):
    
#     c=0
#     while num != 0:
#         c+=1
#         num//=10
#     return c


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

c1=int(input("Enter a number: "))
x=digit_counter(c1)

print(x)