"""
插入排序：每一趟将一个待排序的记录，按照其关键字的大小插入到有序队列的合适位置里，知道全部插入完成。 
假设有一组无序序列 R0, R1, ... , RN-1。
(1) 我们先将这个序列中下标为 0 的元素视为元素个数为 1 的有序序列。
(2) 然后，我们要依次把 R1, R2, ... , RN-1 插入到这个有序序列中。所以，我们需要一个外部循环，从下标 1 扫描到 N-1 。
(3) 接下来描述插入过程。假设这是要将 Ri 插入到前面有序的序列中。由前面所述，我们可知，插入Ri时，前 i-1 个数肯定已经是有序了。
所以我们需要将Ri 和R0 ~ Ri-1 进行比较，确定要插入的合适位置。这就需要一个内部循环，我们一般是从后往前比较，即从下标 i-1 开始向 0 进行扫描。
"""

def inserSort(input_list):
    if len(input_list)==0:
        return []
    for i in range(1,len(input_list)):
        tem=input_list[i]
        j=i-1
        while j>=0 and tem<input_list[j]:
            input_list[j+1]=input_list[j]
            j-=1
        input_list[j+1]=tem
    print(input_list)

a=[6,4,8,9,2,3,1,4]
inserSort(a)

"""
2、时间复杂度
当数据正序时，执行效率最好，每次插入都不用移动前面的元素，时间复杂度为O(N)。 
当数据反序时，执行效率最差，每次插入都要前面的元素后移，时间复杂度为O(N^2)。
所以，数据越接近正序，直接插入排序的算法性能越好。 
3、空间复杂度
由直接插入排序算法可知，我们在排序过程中，需要一个临时变量存储要插入的值，所以空间复杂度为 1 。
4、算法稳定性
直接插入排序的过程中，不需要改变相等数值元素的位置，所以它是稳定的算法。
四、优化
因为在一个有序序列中查找一个插入位置，以保证有序序列的序列不变，所以可以使用二分查找，减少元素比较次数提高效率。
二分查找是对于有序数组而言的，假设如果数组是升序排序的。那么，二分查找算法就是不断对数组进行对半分割，
每次拿中间元素和目标数字进行比较，如果中间元素小于目标数字，则说明目标数字应该在右侧被分割的数组中，如果中间元素大于目标数字，
则说明目标数字应该在左侧被分割的数组中。
"""
def BinarySearch(input_list, end, value):
    left = 0
    right = end - 1
    while left <= right:
        middle = left + (right - left) // 2
        if input_list[middle] >= value:
            right = middle - 1
        else:
            left = middle + 1
 
    return left if left < end else -1
 
def BinaryInsertSort(input_list):
    if len(input_list) == 0:
        return []
    result = input_list
    for i in range(1, len(input_list)):
        j = i - 1
        temp = result[i]
        insert_index = BinarySearch(result, i, result[i])
        if insert_index != -1:
            while j >= insert_index:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = temp
    return result