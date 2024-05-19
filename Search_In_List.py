#Getting list from a user then get a number from user to compare with the list 
def gettinglist(client):

    x=[]

    for _ in range(client):
        client2=int(input("Enter your numbers: "))
        x.append(client2)
    return x


def search_in_list(list,number):

    flag=False

    for i in list:
        if i == number:
            flag=True
    return f"Input value is: {flag} "


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------
      

c1=int(input("How many numbers do you want to put in your list: "))
a=gettinglist(c1)

c2=int(input("What is the number you want to compare with: "))
b=search_in_list(a,c2)


print(b)


















