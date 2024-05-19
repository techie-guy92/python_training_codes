# The code can become your input number to binary
def cal_binary():
    client=int(input("Enter A Number  : "))

    x=1
    binary=0

    while client>0:
        y=client%2
        binary+=x*y
        client//=2
        x*=10

    print()
    print(f"""Binary of your input number is: {binary}
but if it is less than 8 digits or 16 digits you should know there were zero before first one""")

#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

cal_binary()