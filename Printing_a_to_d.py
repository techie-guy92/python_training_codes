#------------------------------------------------------------------------------------------
# This programm can get a string (which is quadruple "a") then move over that until then, 
# which has been already determined.
#------------------------------------------------------------------------------------------

def get_str(mystr):

    mylist=[ord(ch) for ch in mystr]  
    item=len(mylist) - 1 

    while True:
        if mylist[item] + 1 < ord('z') + 1:
            break
        mylist[item]=ord('a')
        item-=1
    mylist[item]+=1
    mylist=[chr(ch) for ch in mylist]

    return ''.join(mylist)
    

def printing_a_to_d(mystr):

    if mystr != "abce":                          
        print(mystr)
        mystr=get_str(mystr)            
        printing_a_to_d(mystr)


#------------------------------------------------------------------------------------------
# Running Code:
# Warnning: Do not input a big value, otherwise you might get error (it is system error)
#------------------------------------------------------------------------------------------

starting_point="aaaa"
# ending_point="abce"
printing_a_to_d(starting_point)                               






