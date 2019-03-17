'''
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。
形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0
'''
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict
        ans = defaultdict(int)
        for t in time:
            ans[t%60] += 1
        return sum(ans[k]*ans[60-k] for k in ans if k>0 and k<30 and (60-k) in ans) + ans[30]*(ans[30]-1)/2+ans[0]*(ans[0]-1)/2

class Solution2:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict
        ans = defaultdict(int)
        num=0
        for i in time:
            i%=60
            num+=ans[(60-i)%60]
            ans[i]+=1
        return num
        