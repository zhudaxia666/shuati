''''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        #在每个位置所能盛水的最大值为该点左边的最大值与右边最大值的最小的一个减去该点高度
        if not height:
            return 0
        max_left=[0]*len(height)
        max_right=[0]*len(height)
        max_left[0]=height[0]
        max_right[-1]=height[-1]
        
        for i in range(1,len(height)):
            max_left[i]=max(height[i],max_left[i-1])
        for j in range(len(height)-2,-1,-1):
            max_right[j]=max(height[j],max_right[j+1])
            
        res=0
        for i in range(len(height)):
            res+=min(max_left[i],max_right[i])-height[i]
        return res