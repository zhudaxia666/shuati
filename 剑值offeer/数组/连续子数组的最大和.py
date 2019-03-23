'''
数组分析：下图是我们计算数组（1，-2，3，10，-4，7，2，-5）中子数组的最大和的过程。通过分析我们发现，累加的子数组和，
如果大于零，那么我们继续累加就行；否则，则需要剔除原来的累加和重新开始
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
