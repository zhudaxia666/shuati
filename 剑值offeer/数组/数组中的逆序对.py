#每次找到最小值，此时的逆序对是最小值的索引，然后删掉最小值，继续上一步
def InversePairs(data):
        if len(data)<=1:
            return 0
        num=0
        while data:
            if sorted(data)==data:
                break
            min_index=data.index(min(data))
            num+=min_index
            data.pop(min_index)
        return num
# l=[1,4,2,6,3,0]
# print(InversePairs(l))

# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
def InversePairs(data):
    # write code here
    if not data:
        return 0
    temp = [i for i in data]
    return mergeSort(temp, data, 0, len(data)-1) % 1000000007
    
def mergeSort(temp, data, low, high):
    if low >= high:
        temp[low] = data[low]
        return 0
    mid = (low + high) / 2
    left = mergeSort(data, temp, low, mid)
    right = mergeSort(data, temp, mid+1, high)
        
    count = 0
    i = low
    j = mid+1
    index = low
    while i <= mid and j <= high:
        if data[i] <= data[j]:
            temp[index] = data[i]
            i += 1
        else:
            temp[index] = data[j]
            count += mid-i+1
            j += 1
        index += 1
    while i <= mid:
        temp[index] = data[i]
        i += 1
        index += 1
    while j <= high:
        temp[index] = data[j]
        j += 1
        index += 1
    return count + left + right
l=[1,4,2,6,3,0]
# a=Solution()
print(InversePairs(l))
''''
交换copy和data是因为：
1.在每次的操作中，数值的比较都是采用当前传入函数中第一项，也就是data；比较的结果都存放到copy中；也就意味着此时copy中是经过此次调用的结果。
2.从最底层返回时，进入了(start == end)的情形，data 和 copy 完全没有修改，此时copy和data还是一样的。
3.进入倒数第二层时，程序进入上图26行以后部分，copy是部分排序后的新数组，data是旧数组。注意这里都是传值的调用，数组都是直接修改的。
倒数第二层使用的copy其实是倒数第三层中的data,这就确保了倒数第三层进入26行以后时，数据比较使用的data是最新排序的数组。
4. 倒数第三层将排序的结果存入copy中。程序在倒数第四层进入26行后，使用的data数组为刚刚倒数第三层中的最新排序的copy.
5. 也就是说，在每次程序进入26行时，此时的data是最新的排序结果，copy是次新的结果。
   在最后一次进入26行以后时，copy为完整排序后的结果，data是次新的结果。
   然而这里第一个类内函数调用第二个函数时，data和copy的顺序没有改变，所以最后结果应该copy是完整排序的结果.data是差一步完成排序的结果。以输入[7,5,6,4], 
   最后的结果copy[4,5,6,7], data[5,7,4,6].
'''
class Solution2:
    def InversePairs(self, data):
        # write code here
        if len(data)<=0:
            return 0
        copy=[i for i in data]
        return self.mergesort(copy,data,0,len(data)-1)%1000000007
    def mergesort(self,copy,data,start,end):
        if start>=end:
            copy[start]=data[start]
            return 0
        mid=(start+end)//2
        left=self.mergesort(data,copy,start,mid)
        right=self.mergesort(data,copy,mid+1,end)
        
        count=0
        i=start
        j=mid+1
        index=start
        while i<=mid and j<=end:
            if data[i]<=data[j]:
                copy[index]=data[i]
                i+=1
            else:
                copy[index]=data[j]
                count+=mid-i+1
                j+=1
            index+=1
        while i<=mid:
            copy[index]=data[i]
            i+=1
            index+=1
        while j<=end:
            copy[index]=data[j]
            j+=1
            index+=1
        return count+left+right