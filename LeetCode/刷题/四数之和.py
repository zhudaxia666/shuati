'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
'''
def FourSum(nums,target):
    results=[]
    if len(nums)<4:
        return results
    nums.sort()
    for i in range(len(nums)-3):
        for j in range(i+1,len(nums) - 2):
            start = j + 1
            end = len(nums) - 1
            while(start < end):
                if(nums[i]+nums[j]+nums[start] + nums[end] == target):
                    lis = []
                    lis.append(nums[i])
                    lis.append(nums[j])
                    lis.append(nums[start])
                    lis.append(nums[end])
                    # 检查结果数组有无重复
                    if lis not in results:
                        results.append(lis)
                    start += 1
                    end -= 1
                # 进行判断，若小于num，首指针前进；反之，尾指针后退
                elif(nums[i]+nums[j]+nums[start] + nums[end] < target):
                    start += 1
                else:
                    end -= 1
    return results



nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(FourSum(nums,target))

