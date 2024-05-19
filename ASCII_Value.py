#First procedure of changing input value to ASCII code

def ascii_value():

    print("Enter a String: ", end="")
    text = input()

    for ch in text:
        asc = ord(ch)
        print(f"""ASCII Value of "{ch}" is "{asc}" """)


# Second procedure

# def ascii_value():

#     print("Enter a Character: ", end="")
#     ch = input()

#     chlen = len(ch)
#     if chlen==1:
#         asc = ord(ch)
#         print(f"""ASCII Value of "{ch}" is "{asc}" """)
#     else:
#         print("oops!!!\nInvalid Input (Input just one character)!")


#Third procedure

# def ascii_value():

#     print("ASCII\t\tCharacter")
#     for i in range(256):
#         ch = chr(i)
#         print(i, "\t\t", ch)


#-----------------------------------------------------------------------------------------------------------
# Running the code: 
#-----------------------------------------------------------------------------------------------------------


ascii_value()