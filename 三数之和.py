# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组
class Solution:
    # 整体思路与Java实现类似：先排序，再通过将三数之和转化成两数之和，循环数组判断；设置首尾指针，双向收缩
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        result = []
        # 若输入数组长度小于3，直接返回空result
        if len(nums) < 3:
            return result
        # 对数组进行排序
        nums.sort()
        for i in range(0,len(nums) - 2):
            num = -nums[i]
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                if(nums[start] + nums[end] == num):
                    lis = []
                    lis.append(-num)
                    lis.append(nums[start])
                    lis.append(nums[end])
                    # 检查结果数组有无重复
                    if lis not in result:
                        result.append(lis)
                    start += 1
                    end -= 1
                # 进行判断，若小于num，首指针前进；反之，尾指针后退
                elif(nums[start] + nums[end] < num):
                    start += 1
                else:
                    end -= 1
        return result


    #---------------------方法2-------------------------------
    # def threeSum(self, nums):
    #     result = list()
    #     if len(nums) < 3:
    #         return result

    #     nums.sort()
    #     for i in range(len(nums)):
    #         if i != 0 and nums[i] == nums[i-1]:
    #             continue

    #         left, right = i+1, len(nums)-1
    #         while left < right:
    #             if nums[i] + nums[left] + nums[right] == 0:
    #                 result.append([nums[i], nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1
    #                 while left < right and nums[left] == nums[left-1]:
    #                     left += 1
    #                 while left < right and nums[right] == nums[right+1]:
    #                     right -= 1
    #             elif nums[i] + nums[left] + nums[right] < 0:
    #                 left += 1
    #             else:
    #                 right -= 1

    #     return result


#---------------方法3-------------------------------------------------
        # nums.sort()
        # # print(nums)
        # results=[]
        # tem=[]
        # for i in range(len(nums)-2):
        #     for j in range(len(nums)-i-2):
        #         tar=0-nums[i]-nums[i+j+1]
        #         if tar in nums[(i+j+2):]:
        #             tem=[nums[i],nums[i+j+1],tar]
        #             if tem not in results:
        #                 results.append(tem)
        # return results
 
a=Solution()
nums = [2, 0, 5, -2, -1, -4,-3,-7]
print(a.threeSum(nums))