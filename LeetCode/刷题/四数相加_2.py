'''
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
'''
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)

        for c in C:
            for d in D:
                lookup[c+d] += 1

        res = 0
        for a in A:
            for b in B:
                res += lookup[-(a+b)]
        return res

def fourSumCount(self, A, B, C, D):
        """
        把 C+D 放入查找表，A和 B用2重循环遍历
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        sum4 = 0

        for c in C:
            for d in D:
                cd = c + d
                if cd not in dic:
                    dic[cd] = 1
                else:
                    dic[cd] += 1

        for a in A:
            for b in B:
                if (-a - b) in dic:
                    sum4 += dic[(-a - b)]

        return sum4