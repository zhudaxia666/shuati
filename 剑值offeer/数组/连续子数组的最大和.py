'''
计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
思路：
数组从左到右累加，先设一个最大累加和，如果在遍历的时候当前累积和大于最大和，就替换最大和，还有
累加的子数组和，如果大于零，那么我们继续累加就行；否则，则需要剔除原来的累加和重新开始
步骤：
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array)==0:
            return 0
        maxsum=array[0]
        cursum=array[0]
        for each in array[1:]:
            if cursum<=0:
                cursum=each
            else:
                cursum+=each
            if cursum>maxsum:
                maxsum=cursum
        return maxsum
