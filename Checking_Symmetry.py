#User can input a word or numbers then the code will diagnose that is symetrical or not  

def checking_symmetry():
 
    x=str(input("Enter a value: "))
    y=x[::-1]

    if x == y:
        return f"Input value is symmetrical"
    else:
        return f"Input value i not asymmetrical"


# Second procedure


# client=str(input("Enter a word: "))

# len_client=len(client)
# x=0
# y=len_client-1

# myinput=True

# while x<y:
#     if client[x]!=client[y]:
#          myinput=False
#          break
#     x+=1;y-=1
    
# print(f"The result of symmetry is: {myinput}")

#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

x=checking_symmetry()
print(x)