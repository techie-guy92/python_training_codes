class myEx(Exception):
    def __init__(self,message) :
        super().__init__(message)
        self.message=message

    def __str__(self):
        return f"Ooops...\n {self.message}"



def email_Validation(email):

    if email[0].isdigit():
        raise myEx("Email cannot start with a number")

    elif email[-10] not in "@": 
        raise myEx("The format of your email is not correct")

    elif email[-1:-9] not in "yahoo.com" or email[-1:-9] not in "gmail.com":
        raise myEx("The format of your email is not correct")
    
    return f"Email: {email}"



def Phone_Number_Validation(phone_number):

    if len(phone_number) != 11:
        raise myEx("Phone Number must be 11 numbers")
    
    elif not phone_number[:12].isdigit():
        raise myEx("Phone number is not valid")
    
    elif phone_number[:4] != "0912" and phone_number[:4] != "0919" and phone_number[:4] != "0935" and phone_number[:4] != "0936" and phone_number[:4] != "0937" and phone_number[:4] != "0938":
            raise myEx("Pre-Number is not valid") 
        
    return f"Phone Number: {phone_number}"


#-------------------------------------------Running program-----------------------------------------------------


try:

    client1=input("Enter your email: ")
    client2=input("Enter your phone number: ")
    checking_email=email_Validation(client1)
    checking_number=Phone_Number_Validation(client2)
    print(checking_email)
    print(checking_number)


    # print(email_Validation("soheil.dalirii@gamil.com"))
    # print(email_Validation("soheil.dalirii@yahoo.com"))
    # print(email_Validation("1soheil.dalirii@gamil.com"))
    # print(email_Validation("soheil.daliriigamil.com"))
    # print(email_Validation("soheil.dalirii@gamil.co"))

    # print(Phone_Number_Validation("09123469239"))
    # print(Phone_Number_Validation("91234692390"))
    # print(Phone_Number_Validation("01234692390"))
    # print(Phone_Number_Validation("1234692390"))
    # print(Phone_Number_Validation("soheil"))

except myEx as error:
    print(error)






