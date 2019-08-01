def find(A,B):
    n1=len(A)
    n2=len(B)
    if n1<2 or n2==0:
        return 0
    for i in range(n1-1):
        if A[i]>=A[i+1]:
            tmp=i
            break
    res=-float('inf')
    if tmp-1==-1:
        val1=res
    else:
        val1=A[tmp-1]
    if tmp+1==(n1-1):
        val2=-res
    else:
        val2=A[tmp+1]
    val3=A[tmp]
    if tmp+2==n1:
        val4=-res
    else:
        val4=A[tmp+2]
    for j in range(n2):
        if B[j]>val1 and B[j]<val2:
            if B[j]>res:
                ans_pos=tmp
            res=max(res,B[j])
        if B[j]>val3 and B[j]<val4:
            if B[j]>res:
                ans_pos=tmp+1
            res=max(res,B[j])
            break
    if res==-float('inf'):
        print('NO')
    else:
        A[ans_pos]=res
        for i in A:
            print(i,end=' ')
# A=list(map(int,input().strip().split()))
# B=list(map(int,input().strip().split()))
A=[1,3,7,7,10]
B=[2,1,5,8,9]
find(A,B)