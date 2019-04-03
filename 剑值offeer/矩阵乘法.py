def matrix(matr1,matr2):
    row1=len(matr1)
    col1=len(matr1[0])
    row2=len(matr2)
    col2=len(matr2[0])
    mat=[[0]*col2 for _ in range(row1) ]
    
    if col1!=row2:
        print('矩阵维度不对')
        return 
    for i in range(row1):
        for k in range(col2):
            sum=0
            for j in range(col1):
                sum+=matr1[i][j]*matr2[j][k]
            mat[i][k]=sum
    return mat

a=[[1,3,5],[2,4,6]]
b=[[1,1,1],[2,2,2],[3,3,3]]
print(matrix(a,b))

        
    
