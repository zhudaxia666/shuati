def find(A,B):
    n1=len(A)
    n2=len(B)
    if n1==0 or n2==0 or n1<2:
        return 0
    for i in range(n1-1):
        if A[i]>=A[i+1]:
            tmp=i
            break
    t=A[tmp]
    # print(tmp,t)
    B=sorted(B)[::-1]
    if n1==2:
        if B[0]>t:
            A[tmp+1]=B[0]
            return 1
        else:
            return 0
    for j in range(n2):
        if tmp==n1-2:
            if B[j]>t:
                A[tmp+1]=B[j]
                return 1
            else:
                return 0
        else:
            if B[j]>t:
                if B[j]<A[tmp+2]:
                    A[tmp+1]=B[j]
                    return 1
                else:
                    continue
            else:
                return 0
A=list(map(int,input().strip().split()))
B=list(map(int,input().strip().split()))
if find(A,B):
    for i in A:
        print(i,end=' ')
else:
    print('NO',end='')