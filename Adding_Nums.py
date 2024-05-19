# The coce can get a str which contain digits and letters then letters are deleted and digits will be added

# def adding_nums(strcontent):

#     x=0
#     y=[]

#     for i in strcontent:
#         if i.isdigit():
#             x=int(i)
#             y.append(x)
    
           
#     return sum(y) 


#second procedure


def adding_nums(strcontent):
    
    x=0

    for i in strcontent:
        if i.isdigit():
            x+=ord(i)-48
    return x            



#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

a=adding_nums("soheil9287omid")
print(a)
