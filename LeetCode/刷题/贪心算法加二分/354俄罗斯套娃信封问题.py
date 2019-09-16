'''
思路：
原问题等价于“将信封数组按照宽“升序”排序以后，信封数组的高的“最长上升子序列”的长度就是题目所求”，在提交的时候，
就会发现出错了。查看错误的测试用例不难发现问题所在，这里我们举例说明问题出在哪里。
事实上，之前我们也已经提到过了：题目要求小信封可以装入大信封的条件是“小信封宽和高分别严格小于大信封的宽和高”。
此时，左边粉红色宽度按照升序排序，但是第 3 个和第 4 个，在宽相等的时候，[6, 7] 和 [6, 8] 会被算法同时选取，
就违背了题意（小信封的宽度和高度分别“严格”小于大信封的宽度和高度）。
解决的办法很容易想到，那就是：在宽度相等的时候，让高度不能出现“上升的子序列”。即首先按照宽度“升序排序”，在宽度相等的时候，
按照高度“降序排序”，这样就能保证宽度相等的信封，最多只能选一个，这种策略保证了结果的正确性。
这就是最开始的说明中的第 1 点缺少的正确性的另一半

'''
class Solution:
    def maxEnvelopes(self,nums):
        size=len(nums)
        if size<2:
            return size
        nums.sort(key=lambda x:(x[0],-x[-1]))
        tail=[nums[0][1]]
        for i in range(1,size):
            target=nums[i][1]
            if target>tail[-1]:
                tail.append(target)
                continue
            l=0
            r=len(tail)-1
            while l<r:
                mid=(left+right)//2
                if tail[mid]<target:
                    l=mid+1
                else:
                    r=mid
            tail[l]=target
        return len(tail)