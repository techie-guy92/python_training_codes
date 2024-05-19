# the code can calculate four main operation in math but user should input a complete operation then put =
def cal_four_main_operation():
	try:

		num1=0
		num2=0
		flag=False

		client=input('Enter a operation: ')

		for op in client:
			if op=='+' or op=='-' or op=='*' or op=='/' :
				operator=op
				flag=True
		
			elif 48<=ord(op) and ord(op)<=57:
				if flag==False:
					num1=num1*10+(ord(op)-48)
				else:
					num2=num2*10+(ord(op)-48)
			elif(op=='='):
				if operator=='+':
					return f"Result of the operation is: {num1+num2}"
				elif operator=='-':
					return f"Result of the operation is: {num1-num2}"
				elif operator=='*':
					return f"Result of the operation is: {num1*num2}"
				elif operator=='/':
					return f"Result of the operation is: {num1/num2}"
					
	except TypeError:
		print("Please correct form of operation\nExample: 20-10=")
	except ValueError:
		print("Please correct form of operation\nExample: 20-10=")
	except OSError:
		print("Please correct form of operation\nExample: 20-10=")


#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

x=cal_four_main_operation()
print(x)	






   