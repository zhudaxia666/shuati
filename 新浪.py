arr=list(map(int,input().split(',')))
arr.sort()
count=0
while True:
    flag=0
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            arr[i+1]+=1
            count+=1
            flag=1
            break
    if flag==0:
        break
    arr.sort()
print(count)