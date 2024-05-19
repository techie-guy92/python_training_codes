try:

    my_list=[]

    
    for _ in range(10): 
       client1=int(input("Enter a number: "))
       my_list.append(client1)
       my_list.sort()

      
    counter=0
    for num in my_list:
        if num == my_list[0]:
            counter+=1
    print(f"""{my_list[0]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[1]:
            counter+=1
    print(f"""{my_list[1]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[2]:
            counter+=1
    print(f"""{my_list[2]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[3]:
            counter+=1
    print(f"""{my_list[3]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[4]:
            counter+=1
    print(f"""{my_list[4]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[5]:
            counter+=1
    print(f"""{my_list[5]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[6]:
            counter+=1
    print(f"""{my_list[6]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[7]:
            counter+=1
    print(f"""{my_list[7]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[8]:
            counter+=1
    print(f"""{my_list[8]} repeated {counter} times""")

    counter=0
    for num in my_list:
        if num == my_list[9]:
            counter+=1
    print(f"""{my_list[9]} repeated {counter} times""")        


except OSError:
    print()
    print("Enter a right value(Numbers)")
except ValueError:
    print()
    print("Enter a right value(Numbers)")
