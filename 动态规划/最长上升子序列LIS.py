'''
一个数的序列bi，当b1 < b2 < … < bS的时候，我们称这个序列是上升的。对于给定的一个序列(a1, a2, …, aN)，
我们可以得到一些上升的子序列(ai1, ai2, …, aiK)，这里1 <= i1 < i2 < … < iK <= N。
比如，对于序列(1, 7, 3, 5, 9, 4, 8)，有它的一些上升子序列，如(1, 7), (3, 4, 8)等等。
这些子序列中最长的长度是4，比如子序列(1, 3, 5, 8).
'''
'''
1.动态规划
状态设计：F[i]代表以A[i]结尾的LIS的长度
状态转移：F[i]=max{F[j]+1}(1<=j< i,A[j]< A[i])
边界处理：F[i]=1(1<=i<=n)
时间复杂度：O(n^2)
'''
def LIS1(A,n):
    r=[1]*n

    for i in range(n):
        for j in range(i):
            if A[i]>A[j]:
                r[i]=max(r[i],r[j]+1)
    print(max(r))
    print(r)
    # return max(r)


#找出并打印
def print_LIS1(A,n):
    r=[1]*n
    pre=[]
    for i in range(n):
        for j in range(i):
            if A[i]>A[j]:
                if r[i]<r[j]+1:
                    pre.append(A[j])
                    r[i]=r[j]+1


    print(max(r))
    print(pre)
a=[1,3,7,2]
print_LIS1(a,len(a))
'''
2.贪心算法+二分法
新建一个low数组，low[i]表示长度为i的LIS结尾元素的最小值。对于一个上升子序列，显然其结尾元素越小，
越有利于在后面接其他的元素，也就越可能变得更长。因此，我们只需要维护low数组，对于每一个a[i]，
如果a[i] > low[当前最长的LIS长度]，就把a[i]接到当前最长的LIS后面，即low[++当前最长的LIS长度]=a[i]。 
那么，怎么维护low数组呢？ 
对于每一个a[i]，如果a[i]能接到LIS后面，就接上去；否则，就用a[i]取更新low数组。具体方法是，
在low数组中找到第一个大于等于a[i]的元素low[j]，用a[i]去更新low[j]。如果从头到尾扫一遍low数组的话，时间复杂度仍是O(n^2)。
我们注意到low数组内部一定是单调不降的，所有我们可以二分low数组，找出第一个大于等于a[i]的元素。
二分一次low数组的时间复杂度的O(lgn)，所以总的时间复杂度是O(nlogn)。
'''
def LIS2(a,n):
    low=[0]*n
    low[0]=a[0]
    end=0
    for i in range(1,n,1):
        if a[i]>low[end]:
            end+=1
            low[end]=a[i]
        else:
            low[binaryser(low,a[i],0,end)]=a[i]
    print(end+1)
    print(low)
    
def binaryser(low,n,left,right):
    while left<right:
        mid=(left+right)//2
        if low[mid]>n:
            right=mid
        else:
            left=mid+1
    return left
    


