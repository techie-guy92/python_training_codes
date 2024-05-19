# There is a Fibonacci class as well as method which users can be used both of the
#----------------------------------------------------------------------------------------------

class Fibonacci:

    def __init__(self,end):
        self.a=0
        self.b=1
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>self.end:
            raise StopIteration
        return self.a

#Running code---------------------------------------------------------------------------------------
client=int(input("Enter a number: "))
fib=Fibonacci(client)

for num in fib:
    print(num)



# Fibonacci function

# def Fibonacci(x):
#     a=0
#     b=1
#     yield b
#     for _ in range(1,x):
#         a,b=b,a+b
#         yield b


# for item in Fibonacci(int(input("Enter a number: "))):
#     print(item,end="    ")

