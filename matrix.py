# CSE 101 HOMEWORK ASSIGNMENT 4
# NAME - SHRAVIKA MITTAL
# ROLL NUMBER - 2016093

# TASK 1

# SUBTASK 1
''' Define the matrix function, ​swapRows(A,row1,row2)​,
that performs a swap between two rows of a given matrix.
The function takes 3 arguments:
    1. A represents the matrix
    2. row1 and row2 are indices of the rows to swap.
    3.​The possible values for the arguments ​row1 ​and row2 ​
    are ​0, ..., nrows - 1, ​ where nrows in number of rows in A   
Sample: A=[[1,2,3],[4,5,6],[7,8,9]] swapRows(A,0,2)
results in A changed to [[7,8,9],[4,5,6],[1,2,3]] '''
def swapRows(A,row1,row2):
    for j in range (len(A[row1])):
        t=A[row1][j]
        A[row1][j]=A[row2][j]
        A[row2][j]=t
    return A



# SUBTASK 2
''' Define a matrix function,​ Row_Transformation(A, x, row1, row2 )​,
that performs row transformation on matrix A
by transforming as row2  →  row2 + x * row1   
Preconditions:
    1. A is a matrix containing integers
    2. x is of type double
    3. The possible values for the arguments ​row1 ​
    and ​row2 ​are ​0, ..., nrows - 1, ​ where nrows in number of rows in A  
Sample: A=[[1,2,3],[4,5,6],[7,8,9]] 
Row_Transformation(A,3,0,2) results in A changed to [[1,2,3],[4,5,6],[10,14,18]]''' 
def Row_Transformation(A,x,row1,row2):
    for j in range (len(A[row1])):
        A[row2][j]=A[row2][j]+x*A[row1][j]
    return A


# SUBTASK 3
'''  define a function that supports finding rank of a given matrix.
In the module define a function ​MatrixRank(A)​ that
    1. takes a nested list A(to represent a matrix) as an argument and
    2. returns an integer representing the rank of A
    3. Preconditions: A is a matrix containing integers ''' 
def MatrixRank(A):
    c=min(len(A),len(A[0]))#rank is minimum of rank and column
    for row in range(c):#finding the row echelon form
        if A[row][row]!=0:
            for k in range(0,len(A)):
                if k!=row:
                    factor=(-(A[k][row]/A[row][row]))
                    Row_Transformation(A,factor,row,k)
        else:
            a=1
            for k in range(row+1,len(A)):
                if A[k][row]!=0:
                    swapRows(A,row,k)
                    a=0
                    break
            if a==1:
                c=c-1
                for j in range(len(A)):
                    s=A[j][row]
                    A[j][row]=A[j][c-1]
                    A[j][c-1]=s
            row=row-1
    r=0
    rank=0
    count=0
    print(A)
    for r in range(len(A)):
        for k in range (len(A[0])):
            if A[r][k]!=0:
                count+=1
        if count>0:
            rank+=1
    return rank
                       
                
