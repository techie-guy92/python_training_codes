#Clients can input day and month then the program can calculate the day of year
def day_counter(day,month):
    
    if 1<=month and month<=6 and 1<=day and day<=31:
      x=(month-1)*31+day

    elif 7<=month and month<=12 and 1<=day and day<=30:
      x=(month-1)*30+6+day

    else:
      print("Error\nPlease enter correct value")

    return x

#-----------------------------------------------------------------------------------------------------------
# Running code:  186 150 
#-----------------------------------------------------------------------------------------------------------

c1=int(input("Enter day: "))
c2=int(input("Enter month: "))

x=day_counter(c1,c2)
print(x)


    