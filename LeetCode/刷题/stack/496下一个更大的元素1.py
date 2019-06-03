'''
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
'''
class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        for v in range(len(nums1)):
            index=nums2.index(nums1[v])
            for i in range(index,len(nums2),1):
                if nums2[i] > nums1[v]:
                    res[v]=nums2[i]
                    break
        return res

#利用栈的思想
'''
遍历一遍 nums 找到 nums 中每个元素与右侧第一个比它大的元素的映射关系，用字典d保存。
栈 s 用来保存那些暂未找到首个比自己大的元素的那些元素。 循环中的每一步，进行如下操作
弹出栈顶元素 key为键，且以nums[i]为值加入字典d直至栈s为空或栈顶元素不小于当前元素s[-1] >= nums[i]。
将当前元素nums[i]入栈。
遍历结束后返回答案 [d[key] if key in d else -1 for key in findNums]
'''
class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l,d=[],{}
        for i in nums2:
            while l and l[-1]<i:
                d[l[-1]]=i
                l.pop()
            l.append(i)
        res=[]
        for i in nums1:
            res.append(d[i] if i in d else -1)
        return res