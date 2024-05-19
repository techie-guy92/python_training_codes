import math


# Function to check if x is power of 2
def isPowerOfTwo():
	c = int(input("Enter a number: "))
	if (c == 0):
		return f""""{False}" is not power of two"""
	while (c != 1):
			if (c % 2 != 0):
				return f""""{False}" is not power of two"""
			c//=2
			
	return f""""{True}" is power of two"""


#second procedure


# Function to check
# Log base 2
# def Log2(x):
# 	return (math.log10(x) / math.log10(2))

# # Function to check
# # if x is power of 2
# def isPowerOfTwo():
#     client = int(input("Enter a number: "))
#     result=math.ceil(Log2(client)) == math.floor(Log2(client))
#     if result == True:
#         return f""""{client}" is power of two"""
#     else:
#         return f""""{client}" is not power of two"""
    
#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------
 

x=isPowerOfTwo()
print(x)
