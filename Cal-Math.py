def calc_math(n):

    def sum(x,y):
        return x+y

    def sub(x,y):
        return x-y

    def mul(x,y):
        return x*y

    def div(x,y):
        return x/y

    if n==1:
        return sum
    elif n==2:
        return sub
    elif n==3:
        return mul
    elif n==4:
        return div


for i in range(1,5):
    z=calc_math(i)
    print(z(20,5))