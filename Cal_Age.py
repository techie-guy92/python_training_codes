from datetime import date


def cal_age(x,c1):

   

    if c1 == "G" or c1 == "g" :
        from datetime import date

        today = date.today()
        age = today.year - x.year - ((today.month, today.day) < (x.month, x.day))
        

        if today.month < x.month:
            left_days=(((12 - x.month) * 30) + (30 - x.day)) + (((today.month - 1) * 30) + today.day)
            
        elif today.month >= x.month:
            left_days=(((today.month - 1) - x.month) * 30) + (30 - x.day + today.day)
            
        elif today.month == x.month and today.day >= x.day:
            left_days=(((today.month - 1) - x.month) * 30) + (30 - x.day + today.day)
            
        elif today.month == x.month and today.day < x.day:
            left_days=(((12 - x.month) * 30) + (30 - x.day)) + (((today.month - 1) * 30) + today.day)

        day_counter= ((age * 365) + left_days) 
        hour_counter= day_counter * 24
        minute_counter= hour_counter * 60  
        second_counter= minute_counter * 60  
           
        return f"""\nYour age is: {age} years old and {left_days} days
Your age by day is: {day_counter}
Your age by hour is: {hour_counter}
Your age by minute is: {minute_counter}
Your age by second is: {second_counter}"""

    
    elif c1 == "S" or c1 == "s" :
        from jdatetime import date

        today = date.today()
        age = today.year - x.year - ((today.month, today.day) < (x.month, x.day))
        

        if today.month < x.month :
            left_days=(((12 - x.month) * 30) + (30 - x.day)) + (((today.month - 1) * 30) + today.day)
            
        elif today.month > x.month :
            left_days=(((today.month - 1) - x.month) * 30) + (30 - x.day + today.day)
            
        elif today.month == x.month and today.day > x.day:
            left_days=(((today.month - 1) - x.month) * 30) + (30 - x.day + today.day)
            
        elif today.month == x.month and today.day < x.day:
            left_days=(((12 - x.month) * 30) + (30 - x.day)) + (((today.month - 1) * 30) + today.day)
            
        
        day_counter= ((age * 365) + left_days) 
        hour_counter= day_counter * 24
        minute_counter= hour_counter * 60  
        second_counter= minute_counter * 60  
           
        return f"""\nYour age is: {age} years old and {left_days} days 
Your age by day is: {day_counter}
Your age by hour is: {hour_counter}
Your age by minute is: {minute_counter}
Your age by second is: {second_counter}"""
    
    else:
        return "\nEnter a correct button"
#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

c1=input("""If you want to enter a gregorian date enter "G"\nIf you want to enter a solar date enter "S"\n""")

year_birth=int(input("Enter date of your brithday\nEnter year of your birth: "))
month_birth=int(input("Enter month of your birth: "))
day_birth=int(input("Enter day of your birth: "))

print(cal_age(date(year_birth, month_birth, day_birth),c1))