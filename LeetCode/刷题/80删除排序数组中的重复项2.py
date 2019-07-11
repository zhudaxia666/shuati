'''

'''
def removeDuplication(self,nums):
    if len(nums)<=2:
        return len(nums)
    #定义两个指针。两指针之间隔一个指针，
    i=0#慢指针
    j=2#快指针
    while j < len(nums):
        if nums[i]!=nums[j]:
            i+=1
            j+=1
        else:
            nums.remove(nums[j])#若相同，就删除nums[j]元素，指针不移动
    return len(nums)