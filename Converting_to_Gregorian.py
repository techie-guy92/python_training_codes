import jdatetime

def converting_to_gregoriancal():

    print("Enter a solar date which you want to convert it to gregorian calendar")
    
    c1=int(input("Enter just a year: "))
    c2=int(input("Enter just a month: "))
    c3=int(input("Enter just a day: "))

    converting=jdatetime.date(c1,c2,c3).togregorian()

    print(f"\nInput date to gregorian calendar is: ",end="")
    return converting


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

x=converting_to_gregoriancal()
print(x)
