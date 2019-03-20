"""
假定在待排序的记录序列中，存在多个具有相同的关键字的记录，若经过排序，这些记录的相对次序保持不变，即在原序列中，
r[i]=r[j]，且r[i]在r[j]之前，而在排序后的序列中，r[i]仍在r[j]之前，则称这种排序算法是稳定的；否则称为不稳定的。
冒泡排序就是把小的元素往前调或者把大的元素往后调。是相邻的两个元素的比较，交换也发生在这两个元素之间。
所以相同元素的前后顺序并没有改变，所以冒泡排序是一种稳定排序算法
"""
#优化：对冒泡排序常见的改进方法是加入标志性变量exchange，用于标志某一趟排序过程中是否有数据交换。
#如果进行某一趟排序时并没有进行数据交换，则说明所有数据已经有序，可立即结束排序，避免不必要的比较过程
def mao_sort(num_list):
    # temp=0
    if len(num_list)==0:
        return []
    # exchange=0
    for i in range(len(num_list)-1):
        exchange=0
        print("这是第%d趟" % (i+1))
        for j in range(len(num_list)-i-1):
            if num_list[j]>num_list[j+1]:
                # temp=num_list[j]
                # num_list[j]=num_list[j+1]
                # num_list[j+1]=temp
                num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
                exchange=1
        if exchange==0:
            break
    #上述代码不能扫描一次就完事，要扫描全部。改进：当冒泡途中发现已经为正序了，就停止对比

    return num_list
a=[1,2,3,4]
print(mao_sort(a))
