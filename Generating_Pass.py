## characters to generate password from
import timeit
beginning = timeit.default_timer()

def generating_pass():
	import string
	import random
	
	
	
	characters = list(string.ascii_letters + string.digits + "!?@#$%&*")
	length = int(input("Enter password length (5 or more): "))
	password=[]
    

	if length >= 5:
		for _ in range(length):
			password.append(random.choice(characters))
		x="".join(password)
		return f"""\nYour complex password is: "{x}"\nDo not share password with anyone else"""
	else:
		return "\nOOPS!!!\nLenght of password must be five or more than five"


ending = timeit.default_timer()


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

print(generating_pass())
print(f"""\nIt took "{ending - beginning}" second to run""")