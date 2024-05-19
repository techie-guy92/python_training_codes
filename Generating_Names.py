# At first function get a list then it can produce random list from first list

# def generating_random_names():
#     import random as rand

#     c1=int(input("How many names do you want to enter: "))
#     my_list=[]

#     for _ in range(c1):
#         y=input("Enter a name: ")
#         my_list.append(y)


#     a=[]
#     b=0
#     c=0

#     while my_list:
#         client=input("""If you want a name type "C": \nif not type "E": \n\n""")
    
#         if client == "c" or client == "e" or client == "C" or client == "E" :
#                 if client == "c" or client == "C":
#                     x=rand.choice(my_list)
#                     b+=1
#                     if x not in a:
#                         a.append(x)
#                         c+=1      
#                 elif client == "e" or client == "E" :
#                     break                       
#         else:
#             print("Error")
#             break

#     return f"{b} names were generated and {b - c} of them were repetitive \nYour random list: {a} "


# second procedure


def generating_random_names():
    import random as rand

    c1=int(input("How many names do you want to enter: "))
    my_list1=[]

    for _ in range(c1):
        y=input("Enter a name: ")
        my_list1.append(y)


    my_list2=[]
    a=0
    b=0
   

    c2=int(input("How many names do you want to be chosen: "))
    while len(my_list2) != c2:

        x=rand.choice(my_list1)
        a+=1
        if x not in my_list2:
            my_list2.append(x)
            b+=1

    return f"{a} names were generated and {a - b} of them were repetitive \nYour random list: {my_list2} "


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------
      
x=generating_random_names()
print(x)



