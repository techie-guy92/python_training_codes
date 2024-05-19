# It can Seprate 3 digits from left then put comma

num=int(input('Enter a number: '))

strNum = str(num)
lenNum = len(strNum)
for i in range(1,lenNum+1) :
	print(strNum[i-1],end='')
	if i % 3 == 0 and i < lenNum:
		print(end=',')

		








