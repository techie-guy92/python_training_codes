def factorial(num):
    
    # num=int(input("Enter a number: "))
    a=num-1

    while a>0:
        num*=a
        a-=1
    return num


#-----------------------------------------------------------------------------------------------------------
# Running the code: 
#-----------------------------------------------------------------------------------------------------------

#print(my_factorial())

for num in range(10):
    print(factorial(num))