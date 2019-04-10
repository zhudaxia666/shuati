import sys
def second(ints,k):
    insert_sort(ints,len(ints))
    if(ints[0] <1):
        return
    flag = 0
    while (k!=0):
        if(ints[len(ints)-1] ==0):
            print(0)
            return
        if (ints[flag]==0):
            while (ints[flag]==0):
                flag+=1
        print(ints[flag])
        for i in range(flag+1,len(ints)):
            ints[i] = ints[i] - ints[flag]
        
        k-=1
        flag+=1
def insert_sort(a, n):
    for i in range(1,n):
        for j in range(i-1,-1,1):
            if a[j]<a[i]:
                break
            if j != i-1:
                temp = a[i]
                for k in range(i-1,j,-1):
                    a[k + 1] = a[k]
                a[k + 1] = temp
if __name__ == "__main__":
    # 读取第一行的n,k
    a = sys.stdin.readline().strip().split()
    n,k=int(a[0]),int(a[1])
    line = sys.stdin.readline().strip()
    arr=list(map(int, line.split()))
    second(arr,k)

# import sys
# def getnum(n,k):
#     i=k
#     m=n
#     med=0
#     while(i!=0):
#         if (m%2)==1:
#             med=m/2+1
#         else:
#             med=m/2
#         m=med
#         if m==1:
#             return i-k+2
#         k-=1
#     return m+k
# # if __name__ == "__main__":
# #     # a = sys.stdin.readline().strip().split()
# #     # n,k=int(a[0]),int(a[1])
# print(getnum(5,4))