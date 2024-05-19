def checking_iterable(obj):

    try:
        iter(obj)
        return f"Input object is iterable"
    except:
        return f"Input object is not iterable"





obj1="soheil"
obj2=12345
obj3=[1,2,3,4,5]
obj4={1,2,3,4,5}
obj5=(1,2,3,4,5)
obj6={1:1,2:2,3:3,4:4,5:5}
obj7=True
obj8=False

print(checking_iterable(obj1))
print(checking_iterable(obj2))
print(checking_iterable(obj3))
print(checking_iterable(obj4))
print(checking_iterable(obj5))
print(checking_iterable(obj6))
print(checking_iterable(obj7))
print(checking_iterable(obj8))