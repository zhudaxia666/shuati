"""
归并排序仍然是利用完全二叉树实现，它是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的
一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列。
基本过程：假设初始序列含有n个记录，则可以看成是n个有序的子序列，每个子序列的长度为1，然后两两归并，
得到n/2个长度为2或1的有序子序列，再两两归并，
最终得到一个长度为n的有序序列为止，这称为2路归并排序。
"""
def mergesort(arr):
    if not arr or len(arr)<2:
        return
    merge_sort(arr,0,len(arr)-1)
def merge_sort(arr,l,r):
    if l==r:
        return
    mid=l+(r-l)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid,r)
    merge(arr,l,mid,r)
def merge(arr,l,m,r):
    tmp=[]
    i=0
    p1=l
    p2=m+1
    while p1<=m and p2<=r:
        if arr[p1]<arr[p2]:
            tmp[i]=arr[p1]
            p1+=1
        else:
            tmp[i]=arr[p2]
            p2+=1
        i+=1
    while p1<=m:
        tmp[i]=arr[p1]
        p1+=1
        i+=1
    while p2<=m:
        tmp[i]=arr[p2]
        p2+=1
        i+=1



'''
第二种办法：
'''


if __name__ == "__main__":
    a=[50,123,543,187,49,30,0,2,11,100]
    mergesort(a)
    print(a)