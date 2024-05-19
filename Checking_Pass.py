def checking_pass():

    my_password="123"
    clients=input("Please enter your password: ")
    
    if clients == my_password:
        return "Welcome to your account"
    elif clients != my_password:
        for _ in range(2): 
            clients=input("oops!!! That was not correct password\nPlease enter your password: ")
            if clients == my_password:
                return "Welcome to your account"
        
        return "It seems you forget your password\nPlease use your email to rest the password"


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

x=checking_pass()
print(x)          
     
