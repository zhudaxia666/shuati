# # def per(nums,p,q,s):
# #     if p==q:
# #         s.append(list(nums))
# #     else:
# #         for i in range(p,q):
# #             nums[i],nums[p]=nums[p],nums[i]
# #             per(nums,p+1,q,s)
# #             nums[i],nums[p]=nums[p],nums[i]
# # s=[]
# # n=int(input())
# # arr=list(map(int,input().split()))
# # nums=[i for i in range(1,n+1)]
# # per(nums,0,len(arr),s)
# # s.sort()
# # if arr in s:
# #     index=s.index(arr)
# #     for i in s[-(index+1)]:
# #         print(i,end=' ')
# # print(s)
# t=int(input())
# res=[]
# for i in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     flag=0
#     for j in range(1,n-1):
#         if arr[j]>arr[j-1]+arr[j+1]:
#             flag=1
#             break
#     if flag:
#         res.append('NO')
#     else:
#         if arr[0]>arr[-1]+arr[1] or arr[-1]>arr[-2]+arr[0]:
#             res.append('NO')
#         elif arr[0]<arr[-1]+arr[1] and arr[-1]<arr[-2]+arr[0]:
#             res.append('YES')
# for i in res:
#     print(i)

# import random
#改进后的快速排序，类似于荷兰国旗问题，和一般的排序区别在于，一般的快排是只排一个元素，而改进后，可以把多个元素都比较出来
# def quick_sort(arr,l,r):
#     if l<r:
#         #下面两行代码是产生随机一个数，然后与数组最后一个元素比较,该方法为随机快排，去掉下面两行也没问题
#         # rand=l+int(random.random()*(r-l+1))
#         # arr[rand],arr[r]=arr[r],arr[rand]

#         p=partition(arr,l,r)
#         quick_sort(arr,l,p[0]-1)
#         quick_sort(arr,p[1]+1,r)
# def partition(arr,l,r):#以最后一个位置为划分
#     less=l-1
#     more=r
#     while l<more:
#         if arr[l]<arr[r]:
#             less+=1
#             l+=1
#         elif arr[l]>arr[r] and (arr[l]+arr[r])%2==1:
#             more-=1
#             arr[more],arr[l]=arr[l],arr[more]
#         else:
#             l+=1
#     # arr[more],arr[r]=arr[r],arr[more]
#     return [less+1,more]
# if __name__ == "__main__":
#     # arr = [8, 3, 1, 6, 4, 7, 3, 14, 13]
#     arr=[53941,38641,31525,75864,29026,12199,83522,58200,64784,80987]
#     l=0
#     r=len(arr)-1
#     quick_sort(arr,l,r)
#     print(arr)
def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]