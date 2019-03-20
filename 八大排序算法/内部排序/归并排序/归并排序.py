"""
归并排序仍然是利用完全二叉树实现，它是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的
一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列。
基本过程：假设初始序列含有n个记录，则可以看成是n个有序的子序列，每个子序列的长度为1，然后两两归并，
得到n/2个长度为2或1的有序子序列，再两两归并，
最终得到一个长度为n的有序序列为止，这称为2路归并排序。
"""

def merge_sort(input_list):
    if len(input_list)<=1:
        return input_list
    
    mid=len(input_list)//2
    
    left=merge_sort(input_list[:mid])
    right=merge_sort(input_list[mid:])
# 这里记录一下，python有一个模块，专门提供了归并排序的方法，叫做“heapq”模块，因此我们只要将分解后的结果导入该方法即可
    return merge1(left,right)

def merge1(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])   
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    a=[50,123,543,187,49,30,0,2,11,100]
    print(merge_sort(a))