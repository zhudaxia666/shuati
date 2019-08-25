import random
def quick_sort(arr,l,r,res):
    if l<r:
        #下面两行代码是产生随机一个数，然后与数组最后一个元素比较,该方法为随机快排，去掉下面两行也没问题
        rand=l+int(random.random()*(r-l+1))
        arr[rand],arr[r]=arr[r],arr[rand]
        p=partition(arr,l,r)
        res.append(p)
        quick_sort(arr,l,p[0]-1,res)
        quick_sort(arr,p[1]+1,r,res)
def partition(arr,l,r):#以最后一个位置为划分
    less=l-1
    more=r
    while l<more:
        if arr[l]>arr[r]:
            less+=1
            arr[less],arr[l]=arr[l],arr[less]
            l+=1
        elif arr[l]<arr[r]:
            more-=1
            arr[more],arr[l]=arr[l],arr[more]
        else:
            l+=1
    arr[more],arr[r]=arr[r],arr[more]
    return [less+1,more]
if __name__ == "__main__":
    # arr = [8, 3, 1, 6, 4, 7, 3, 14, 13]
    arr=['waimai','dache','lvyou','liren','meishi','jiehun','lvyouing','lvyoujingdian','jiaopei','menpiao','jiudian',]
    l=0
    r=len(arr)-1
    res=[]
    quick_sort(arr,l,r,res)
    print(arr)
    print(res)
    count=len(arr)-1
    for i in range(len(arr)-1,0,-1):
        if arr[i] in [' ','']:
            count=i
    for i in range(count-1,0,-1):
        if arr[i] in arr[i-1]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
    print(arr[count:]+arr[:count])
