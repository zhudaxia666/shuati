'''
基数排序(Radix Sort)是桶排序的扩展，它的基本思想是：将整数按位数切割成不同的数字，然后按每个位数分别比较。
具体做法是：将所有待比较数值统一为同样的数位长度，数位较短的数前面补零。然后，从最低位开始，依次进行一次排序。
这样从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列。
'''
# -*- coding:utf-8 -*-

def RadixSort(input_list):
	'''
	函数说明:基数排序（升序）
	Author:
		www.cuijiahua.com
	Parameters:
		input_list - 待排序列表
	Returns:
		sorted_list - 升序排序好的列表
	'''
	def MaxBit(input_list):
		'''
		函数说明:求出数组中最大数的位数的函数
		Author:
			www.cuijiahua.com
		Parameters:
			input_list - 待排序列表
		Returns:
			bits-num - 位数
		'''
		max_data = max(input_list)
		bits_num = 0
		while max_data:
			bits_num += 1
			max_data //= 10
		return bits_num

	def digit(num, d):
		'''
		函数说明:取数xxx上的第d位数字
		Author:
			www.cuijiahua.com
		Parameters:
			num - 待操作的数
			d - 第d位的数
		Returns:
			取数结果
		'''	
		p = 1
		while d > 1:
			d -= 1
			p *= 10
		return num // p % 10


	if len(input_list) == 0:
		return []
	sorted_list = input_list#
	length = len(sorted_list)
	bucket = [0] * length# // 临时数组，用来存放排序过程中的数据
	#从低位往高位循环
	for d in range(1, MaxBit(sorted_list) + 1):
		count = [0] * 10#// 位记数器，从第0个元素到第9个元素依次用来记录当前比较位是0的有多少个...是9的有多少个数
        #//// 统计各个桶中的个数
		for i in range(0, length):
			count[digit(sorted_list[i], d)] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		for i in range(0, length)[::-1]:
			k = digit(sorted_list[i], d)
			bucket[count[k] - 1] = sorted_list[i]
			count[k] -= 1
		for i in range(0, length):
			sorted_list[i] = bucket[i]

	return sorted_list

def radix_sort(a):
    i=0 #初始为个位排序
    n=1#表示位数
    max_num=max(a)
    while max_num > 10**n:
        n+=1
    while i<n:
        bucket={}#用字典构建桶
        for x in range(10): #将每个桶置空
            bucket.setdefault(x,[])
        for x in a:
            radix=int((x/(10**i))%10)#得到每位的基数
            bucket[radix].append(x)#将对影的数字化元素加到相对应的位基数的桶中
        j=0
        for k in range(10):
            if len(bucket[k])!=0:   #若桶不为空
                for y in bucket[k]:  #将该桶中每个元素放回数组
                    a[j]=y
                    j+=1
        i+=1
    return a



input_list = [50,123,543,187,49,30,0,2,11,100]
print(radix_sort(input_list))

# if __name__ == '__main__':
# 	input_list = [50,123,543,187,49,30,0,2,11,100]
#     print(radix_sort(input_list))
# 	# print('排序前:', input_list)
# 	# # sorted_list = RadixSort(input_list)
#     # sorted_list = radix_sort(input_list)
# 	# print('排序后:', sorted_list)