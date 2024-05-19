#---------------------------------------------------------------------------------------------------------
# The code gets number of queens as an input then demonstrat how to place them which each queen does not
# threat each other.
#---------------------------------------------------------------------------------------------------------

input_value= int(input("Enter the number of queens: "))

# here we create a chessboard
# NxN matrix with all elements set to 0
board = [[0]*input_value for _ in range(input_value)]


def attack(i, j):
    #checking vertically and horizontally
    for k in range(0,input_value):
        if board[i][k]==1 or board[k][j]==1:
            return True

    #checking diagonally
    for k in range(0,input_value):
        for l in range(0,input_value):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False


def N_queens(n):
    if n==0:
        return True
    for i in range(0,input_value):
        for j in range(0,input_value):
            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queens(n-1)==True:
                    return True
                board[i][j] = 0
    return False

#---------------------------------------------------------------------------------------------------------
# Running code: 
#---------------------------------------------------------------------------------------------------------

N_queens(input_value)
for i in board:
    print (i)