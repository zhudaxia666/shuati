'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路：
所谓的一个数m是另一个k数n的因子，是指n能被m整除，也就是n%m==0。根据丑数的定义，
丑数只能被2、3和5整除。根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。
因此我们可以创建一个数组，里面的数字是排好序的丑数，每一个丑数都是前面的丑数乘以2、3或者5得到的。
这个思路的关键问题在于怎样保证数组里面的丑数是排好序的。对乘以2而言，肯定存在某一个丑数T2，
排在它之前的每一个丑数乘以2得到的结果都会小于已有最大的丑数，在它之后的每一个丑数乘以乘以2得到的结果都会太大。
我们只需要记下这个丑数的位置，同时每次生成新的丑数的时候，去更新这个T2。对乘以3和5而言，也存在着同样的T3和T5。
注意：1，2，3，4，5，6都是丑数。所以当index小于7的时候，直接返回index即可。
'''
''''
因为丑数只包含质因子2，3，5，假设我们已经有n-1个丑数，按照顺序排列，且第n-1的丑数为M。那么第n个丑数一定是由这n-1个丑数分别乘以2，3，5，
得到的所有大于M的结果中，最小的那个数。
事实上我们不需要每次都计算前面所有丑数乘以2，3，5的结果，然后再比较大小。因为在已存在的丑数中，一定存在某个数T2，在它之前的所有数乘以2都小于已有丑数，
而T2×2的结果一定大于M，同理，也存在这样的数T3，T5T3，T5，我们只需要标记这三个数即可。
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<7:
            return index
        res=[1,2,3,4,5,6]
        t2,t3,t5=3,2,1
        for i in range(6,index):
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            while res[t2]*2<=res[i]:
                t2+=1
            while res[t3]*3<=res[i]:
                t3+=1
            while res[t5]*5<=res[i]:
                t5+=1
        return res[index-1]

# -*- coding:utf-8 -*-
class Solution1:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        # 1作为特殊数直接保存
        baselist = [1]
        min2 = min3 = min5 = 0
        curnum = 1
        while curnum < index:
            minnum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(minnum)
            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while baselist[min2] * 2 <= minnum:
                min2 += 1
            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while baselist[min3] * 3 <= minnum:
                min3 += 1
            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while baselist[min5] * 5 <= minnum:
                min5 += 1
            curnum += 1
        return baselist[-1]
