#The code gets several numbers from a client then it will print two biggest ones


# def cal_biggest_nums():
#     client=int(input("Enter numbers: "))

#     penultimate=0
#     biggest=0


#     while client >= 0 :

#         if client>biggest:
#             penultimate=biggest
#             biggest=client

#         elif client>penultimate:
#             penultimate=client 

#         client=int(input("Enter numbers: "))
        
        

#     return f"""The penultimate number was entered: {penultimate}
# The biggest number was entered: {biggest}"""


# Second procedure


def cal_biggest_nums():

    client=int(input("Enter a number: "))
    my_list=[]

    while client >= 0:
        my_list.append(client)
        client=int(input("Enter a number: "))

    my_set=set(my_list)
    my_list=list(my_set)
    biggest=max(my_list)
    my_list.remove(max(my_list))
    penultimate=max(my_list)
    


    return f"""The penultimate number was entered: {penultimate}
The biggest number was entered: {biggest}"""

#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------


x=cal_biggest_nums()
print(x)