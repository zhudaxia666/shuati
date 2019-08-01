'''
有一天小M得到了n根木棍，并且知道每个木棍的长度。现在她想从这n根木棍中选出3根来作
为三角形的边构成一个三角形，请你帮她判断一下她能否完成这件事
'''
def san(arr):
    if len(arr)<3:
        return False
    a=sorted(arr)
    for i in range(len(arr)-2):#最长的边小于其余两边的和
        if a[i]+a[i+1]>a[i+2]:
            return True
    return False

def san1(arr):
    if len(arr)<3:
        return False
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                s=arr[i]+arr[j]+arr[k]
                m=max(arr[i],max(arr[j],arr[k]))
                if s-m>m:
                    return True
    return False




a=[1,1,1]
print(san1(a))
a=[3,1,10,5,15]
b=[3,4,72,6,4]
print(san1(a))
print(san1(b))
    