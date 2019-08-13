 '''
 给定一个数组，求如果排序之后，相邻两数的最大差值，要求时间复杂度O(n),且要求不能用非基于比较的排序
 思路：使用桶的概念，假设数组有n个数，建立n+1个桶，即划分为n+1等分，设置三个数组，分别表示桶是否装数据，以及桶的最大值和最小值，
 由于有一个空桶，则两数的最大差值一定不会出现在一个桶内，最大差值来自非空桶前一个桶的最大值与后一个非空桶的最小值的差值。遍历完所有桶就得出最大差值
 '''
 def maxgap(nums):
    if not nums or len(nums)<2:
         return 0
    min_num=min(nums)
    max_num=max(nums)

    if min==max:
        return 0
    hasnum=[0]*len(nums)+1
    maxs=[0]*len(nums)+1
    mins=[0]*len(nums)+1

    bid=0
    for i in range(len(nums)):
        bid=((num-min_num)*len(nums)//(max_num-min_num))
        if hasnum:
            mins[bid]=min(mins[bid],nums[i])
            maxs[bid]=max(maxs[bid],nums[i])
        else:
            mins[bid]=nums[i]
            maxs[bid]=nums[i]
        hasnum[bid]=1
    res=0
    lastmax=maxs[0]
    for i in range(1,len(nums)+1):
        if hasnum[i]:
            res=max(res,mins[i]-lastmax)
            lastmax=res
    return res

        
