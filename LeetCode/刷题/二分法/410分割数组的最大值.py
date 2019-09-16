'''
二分逼近法：
思路：先假设找到了最大值的最小值x，反过来算划分的组数。如果组数小于m，说明x还可以再小，组数大于m，说明x要变大，
如果组数等于m，x可能再小
考虑边界情况，把每个元素分成一组，那么x的最小值就是数组的最大值，把数组当做一个组，那个x就是数组元素之和，即max(nums)<=x<=sum(nums)
反过来算划分组数，其实很好理解因为每一组都是连续的，只要每一组累加的和大于了x，那么当前元素就要放到下一组，记录有多少组即可

做的时候有些困惑，这样二分下去，找到了值会不会不是某个组的和？
有这样的顾虑，可能思路还没有从二分查找转化到二分逼近，或者说对二分法理解还不是够深入。二分法本质是缩小范围，二分逼近关键就
在于这个“逼近”，这道题是在连续的数值范围中逼近，换句话说，每个组的和一定在范围之内，因此正确答案是不会被跳过的；而二分查找的数组虽然有序，但数值可能不连续，因此可能会产生误导。
另外一个误区可能是，对于某个逼近的x，它的组数也是m，但这个x不一定是答案，它还可能更小，因此跳出逼近的条件是left>=right
（其实left应该只可能等于right，也就是说一定会逼近到最后一个值，这也许是二分逼近法的核心吧），而不是countGroup(mid)==m。
在代码中可以注意到的细节是，left会跳过不满足条件的mid，而right会保留满足条件的mid，直到找到更小的满足条件的mid。

'''
def splitArray(nums,m):
    length=len(nums)
    def countgroup(mid):
        c=0
        s=0
        for i in range(length):
            s+=nums[i]
            if s>mid:
                s=nums[i]
                c+=1
                if c>m:
                    return c
        return c+1
    left=max(nums)
    right=sum(nums)
    while left<right:
        mid=(left+right)//2
        c=countgroup(mid)
        if c>m:
            left=mid+1
        else:
            right=mid
    return left
                
