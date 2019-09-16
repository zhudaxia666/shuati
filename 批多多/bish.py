import random
def quick_sort(arr,l,r):
    if l<r:
        #下面两行代码是产生随机一个数，然后与数组最后一个元素比较,该方法为随机快排，去掉下面两行也没问题
        rand=l+int(random.random()*(r-l+1))
        arr[rand],arr[r]=arr[r],arr[rand]

        p=partition(arr,l,r)
        quick_sort(arr,l,p[0]-1)
        quick_sort(arr,p[1]+1,r)
def partition(arr,l,r):#以最后一个位置为划分
    less=l-1
    more=r
    while l<more:
        if arr[l]<arr[r]:
            less+=1
            arr[less],arr[l]=arr[l],arr[less]
            l+=1
        elif arr[l]>arr[r]:
            more-=1
            arr[more],arr[l]=arr[l],arr[more]
        else:
            l+=1
    arr[more],arr[r]=arr[r],arr[more]
    return [less+1,more]
if __name__ == "__main__":
    s,n=input().split(';')
    s=list(map(int,s.split(',')))
    n=int(n)
    arr1=[]
    arr2=[]
    for i in s:
        if i&1==1:
            arr1.append(i)
        else:
            arr2.append(i)
    quick_sort(arr1,0,len(arr1)-1)
    quick_sort(arr2,0,len(arr2)-1)
    arr1[:]=arr1[::-1]
    arr2[:]=arr2[::-1]
    if n<=len(arr2):
        for i in range(n):
            print(arr2[i],end=',')
    else:
        for i in range(len(arr2)):
            print(arr2[i],end=',')
        for j in range(n-len(arr2)-1):
            print(arr1[j],end=',')
        print(arr1[n-len(arr2)-1])