
def reversing_data(new_input_value):

    if len(new_input_value) == 0:
        print("")

    else:
        reversing_data(new_input_value[1:])
        print(new_input_value[0],end="\t")


def changing_type(input_value):

    if type(input_value) == str:
        reversing_data(input_value)

    elif type(input_value) == int:
        new_input_value=str(input_value)
        reversing_data(new_input_value)
        
    elif type(input_value) == list:
        new_input_value = ' '.join([str(my_str) for my_str in input_value])
        reversing_data(new_input_value)

#===========================================Running Program=================================================   

try:
    x=[1,2,3,4,5]
    # x=12345
    # x="12345"
    # x="soheil"
    changing_type(x)

except RuntimeError as error:
    print(error)




