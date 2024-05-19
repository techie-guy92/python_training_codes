# def My_Sort(list1):

#     list2=[]

#     for _ in range(len(list1)):
#         list2.append(min(list1))
#         list1.remove(min(list1))

#     return list2


#second procedure

def My_Sort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(0,i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]

    return list1


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

x=My_Sort([189,172,161,182,192,173,188,165,156,197,167,175])
print(x)