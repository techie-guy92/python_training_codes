def building_diamond():
    
    client = eval(input("Enter diamond's height: "))
    for x in range(client):
        print(" " * (client - x), "*" * (2*x + 1))
        
    for x in range(client - 2, -1, -1):
        print(" " * (client - x), "*" * (2*x + 1))

#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

building_diamond()








