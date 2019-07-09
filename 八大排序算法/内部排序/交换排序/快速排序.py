"""
快速排序的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分：分割点左边都是比它小的数，右边都是比它大的数。
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""
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

if __name__ == "__main__":
    input_list=[3,1,2,5,6,9,4]
    left=0
    right=len(input_list)-1
    quicksort(input_list,left,right)
    print(input_list)