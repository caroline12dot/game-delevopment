matrix=[[1,4,6],[2,5,7],[3,8,9]]
print(matrix)
#number of rows
print(len(matrix))
#number of colums
print(len(matrix[1]))
#access the element
print(matrix[2][1])
print(matrix[1][0])

rows=int(input("enter the number of rows "))
colums=int(input("enter the number of colums "))
temp=[]
for i in range(rows):
    row=[]
    for y in range(colums):
        col=int(input("enter an element "))
        row.append(col)
    temp.append(row)
for i in range(rows):
    for y in range(colums):
        print(temp[i][y],end=" ")
    print()
matrixa=[[1,2],[3,4]]
matrixb=[[5,6],[7,8]]
add=[[0,0],[0,0]]
subtrat=[[0,0],[0,0]]
for i in range(2):
    for y in range(2):
        add[i][y]=matrixa[i][y]+matrixb[i][y]
        subtrat[i][y]=matrixa[i][y]-matrixb[i][y]
for i in range(2):
    for y in range(2):
        print(add[i][y],end=" ")
    print()
    
for i in range(2):
    for y in range(2):
        print(subtrat[i][y],end=" ")
    print()

    