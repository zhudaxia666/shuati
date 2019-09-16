
nums=list(input().split(','))
s=''
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
            nums[i],nums[j]=nums[j],nums[i]
for i in nums:
    s+=str(i)
print(str(int(s)))