#------------------------------------------------------------------------------------------
# This programm can get a string (which is four numbers) then move over that until then, 
# which has been already determined.
#------------------------------------------------------------------------------------------

def get_num(mystr): 

    mylist=[int(ch) for ch in mystr]   
    item=len(mylist) - 1 

    while True:
        if mylist[item] + 1 < 10:
            break
        mylist[item]=0
        item-=1
    mylist[item]+=1
    mylist=[str(ch) for ch in mylist]

    return ''.join(mylist)
    

def print_num(mystr):

    if mystr != '0499' :                     #end of the string
        print(mystr)
        mystr=get_num(mystr)            
        print_num(mystr)


#------------------------------------------------------------------------------------------
# Running Code:
# Warnning: Do not input a big value, otherwise you might get error (it is system error) 
#------------------------------------------------------------------------------------------

print_num('0000')                         #beginning of string



