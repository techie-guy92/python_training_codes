#input number will be printed as a reverse

def reverse_number(num):

    a=num%10
    b=num//10
    c=str(a)+str(b)

    return c

#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

c1=int(input("Enter a number: "))
x=reverse_number(c1)
print(x)