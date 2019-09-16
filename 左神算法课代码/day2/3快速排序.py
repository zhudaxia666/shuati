"""
快速排序的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分：分割点左边都是比它小的数，右边都是比它大的数。
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""
'''
当数组是有序时，时间复杂度是O(n^2).
改进：随机快排。随机取一个数，与最后一个元素交换，以该元素作为基准元素，进行比较，此时是求时间复杂度就是个概率问题
此时时间复杂度是O(nlogn),空间复杂度是o(logn),空间复杂度解释，记录了划分点
'''
#一般的快速排序
def quicksort(inputlist,left,right):
    if left<right:
        base_index=division(inputlist,left,right)
        quicksort(inputlist,left,base_index-1)
        quicksort(inputlist,base_index+1,right)
def division(inputlist,left,right):
        base=inputlist[left]
        while(left<right):
            while left<right and inputlist[right]>=base:
                right-=1
            inputlist[left]=inputlist[right]
            while left<right and inputlist[left]<=base:
                left+=1
            inputlist[right]=inputlist[left]
        inputlist[left]=base
        return left
import random
#改进后的快速排序，类似于荷兰国旗问题，和一般的排序区别在于，一般的快排是只排一个元素，而改进后，可以把多个元素都比较出来
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
    print(less+1,more)
    return [less+1,more]
if __name__ == "__main__":
    # arr = [8, 3, 1, 6, 4, 7, 3, 14, 13]
    arr=[4,36,2,4,23,54,2,4]
    l=0
    r=len(arr)-1
    quick_sort(arr,l,r)
    print(arr)
