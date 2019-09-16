'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

我们要知道IP的格式,每位是在0~255之间,
注意: 不能出现以0开头的两位以上数字,比如012,08...
思路一:暴力法
我们把所有出现可能都列举出来,看是否满足条件.

思路二:回溯算法

'''
#思路1：
def fun1(s):
    n=len(s)
    res=[]
    #判断ip是否满足ip的条件
    def helper(tmp):
        if not tmp or (len(s)>1 and tmp[0]=='0') or int(tmp)>255:
            return False
        return True
    #三个循环把数字分成四部分
    for i in range(3):
        for j in range(i+1,i+4):
            for k in range(j+1,j+4):
                if i<n and j<n and k<n:
                    tmp1=s[:i+1]
                    tmp2=s[i+1:j+1]
                    tmp3=s[j+1:k+1]
                    tmp4=s[k+1:]
                    if all(map(helper,[tmp1,tmp2,tmp3,tmp4])):
                        res.append(tmp1+'.'+tmp2+'.'+tmp3+'.'+tmp4)
    return res

#回溯法
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/restore-ip-addresses/solution/bao-li-he-hui-su-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。