import jdatetime

def converting_to_solarcal():

    print("Enter a gregorian date which you want to convert it to solar calendar")
    
    c1=int(input("Enter just a year: "))
    c2=int(input("Enter just a month: "))
    c3=int(input("Enter just a day: "))

    converting=jdatetime.date.fromgregorian(day=c3,month=c2,year=c1)

    print(f"\nInput date to solar calendar is: ",end="")
    return converting

    
#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

x=converting_to_solarcal()
print(x)