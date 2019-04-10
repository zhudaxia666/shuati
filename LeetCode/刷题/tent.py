import sys

def jianfa(arr,k):
    min_index=arr.index(min(arr))
    flag=True
    # tem=arr.pop(min_index)
    for i in range(k):
        if flag:
            if arr[min_index]>0:
                print(arr[min_index])
        #tem=arr.pop(min_index)
        if not flag:
            for i in range(len(arr)):
                arr[i]=
            num=0
            t=arr-l
            for i in t:
                if i==0:
                    num+=1
                else:
                    print(i,end=' ')
            if num==len(l):
                print(0)
                break
        flag=not flag
if __name__ == "__main__":
    # 读取第一行的n,k
    a = sys.stdin.readline().strip().split()
    n,k=int(a[0]),int(a[1])
    line = sys.stdin.readline().strip()
    arr=list(map(int, line.split()))
    jianfa(arr,k)