# The code is magic square 
# It can create a square which all the columns and rows are equal if they are calculated

def magic_squre():

	n=int(input("Enter Number Of Row And Col : "))
	a = [[0 for i in range(n)] for j in range(n)] 
	count=1
	if(n%2==1):
		i=0
		j=n//2
		print(i,j)
		a[i][j]=count
		count+=1
		while(count<=n*n):
			x=i-1
			y=j+1
			if(x<0 and y==n):
				x=i+1
				y=j
			elif(x<0):
				x=n-1
				i=x
			elif(y==n):
				y=0
				j=y
			elif(a[x][y]!=0):
				x=i+1
				y=j
			a[x][y]=count
			count+=1
			i=x
			j=y
	
		for i in range(0,n):
			for j in range(0,n):
				print(a[i][j],end="\t")
			print() 
	else:
		print("Number should be odd")



#-----------------------------------------------------------------------------------------------------------
# Running code: 
#-----------------------------------------------------------------------------------------------------------

magic_squre()
