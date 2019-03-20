"""
简单排序很简单，它的大致处理流程为：

    从待排序序列中，找到关键字最小的元素；
    如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；
    从余下的 N - 1 个元素中，找出关键字最小的元素，重复(1)、(2)步，直到排序结束。
"""
def xuzesort(intput_list):
    if len(intput_list)<=1:
        return intput_list
    for i in range(len(intput_list)-1):
        print("这是第%d趟" % (i+1))
        # minnum=intput_list[i]
        index=i
        for j in range(len(intput_list)-i-1):
            if intput_list[index]>intput_list[i+j+1]:
                # minnum=intput_list[i+j+1]
                index=i+j+1
        if index!=i:
            intput_list[i],intput_list[index]=intput_list[index],intput_list[i]
        print(intput_list)

# -*- coding:utf-8 -*-
 
def SelectSort(input_list):
    '''
    函数说明:简单选择排序（升序）
    Author:
        www.cuijiahua.com
    Parameters:
        input_list - 待排序列表
    Returns:
        sorted_list - 升序排序好的列表
    '''    
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    length = len(sorted_list)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if sorted_list[min_index] > sorted_list[j]:
                min_index = j
        if min_index == i:
            continue
        temp = sorted_list[i]
        sorted_list[i] = sorted_list[min_index]
        sorted_list[min_index] = temp
    return sorted_list

if __name__ == "__main__":
    a=[6,4,8,9,2,3,1]
    xuzesort(a)

"""
2、时间复杂度

简单选择排序的比较次数与序列的初始排序无关。 假设待排序的序列有 N 个元素，则比较次数总是N (N - 1) / 2。
而移动次数与序列的初始排序有关。当序列正序时，移动次数最少，为 0.
当序列反序时，移动次数最多，为3N (N - 1) /  2。
所以，综合以上，简单排序的时间复杂度为 O(N^2)。
3、空间复杂度
简单选择排序需要占用 1 个临时空间，用于保存最小值得索引。
"""