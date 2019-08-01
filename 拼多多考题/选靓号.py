''''
A 国的手机号码由且仅由 N 位十进制数字(0-9)组成。一个手机号码中有至少 K 位数字相同则被定义为靓号。A 国的手机号可以有前导零，比如 000123456 是一个合法的手机号。
小多想花钱将自己的手机号码修改为一个靓号。修改号码中的一个数字需要花费的金额为新数字与旧数字之间的差值。比如将 1 修改为 6 或 6 修改为 1 都需要花 5 块钱。
给出小多现在的手机号码，问将其修改成一个靓号，最少需要多少钱？

输入描述:
第一行包含2个整数 N、K，分别表示手机号码数字个数以及靓号至少有 K 个数字相同。
第二行包含 N 个字符，每个字符都是一个数字('0'-'9')，数字之间没有任何其他空白符。表示小多的手机号码。
数据范围：
2 <= K <= N <= 10000

输出描述:
第一行包含一个整数，表示修改成一个靓号，最少需要的金额。
第二行包含 N 个数字字符，表示最少花费修改的新手机号。若有多个靓号花费都最少，则输出字典序最小的靓号。
示例1
输入
6 5
787585
输出
4
777577

思路：
"""
最小修改距离，
先找最小修改距离ans_cost下，相同的数字ans_num
再求以ans_num为修改目标，当修改值大于ans_num时从前往后修改，
当修改值小于ans_num时从后往前修改
"""
'''
from collections import Counter

def distance(dic,k,t):#找以t为重复值的最少花费
    ret=0
    if dic[t]>=k:
        return ret
    k-=dic[t]
    for i in range(1,10):#以t为起点左右找修改所需要最少花费
        if t+i<10:#
            if dic[t+i]>=k:
                ret+=i*k
                return ret
            else:
                k-=dic[t+i]
                res+=i*dic[t+i]
        if t-i>=0:
            if dic[t-i]>=k:
                ret+=i*k
                return ret
            else:
                k-=dic[t-i]
                res+=i*dic[t-i]
def modify(s,dic,k,t):
    if dic[t]>=k:
        return
    k-=dic[t]
    for i in range(1,10):
        if t+i<10:
            for j in range(len(s)):
                if k==0:
                    return 
                if s[j]==t+i:
                    s[j]=t
                    k-=1
        if t-i>=0:
            for j in range(len(s)-1,-1,-1):
                if k==0:
                    return
                if s[j]==t-i:
                    s[j]=t
                    k-=1
if __name__ == "__main__":
    n,k=map(int,input().strip().split())
    s=list(map(int,list(input().strip())))
    dic=Counter(s)
    for i in range(10):
        if i not in dic:
            dic[i]=0
    cost,num=float('inf'),-1
    for i in range(10):
        tmp=distance(dic,k,i)
        if tmp<cost:
            cost=tmp
            num=i
    modify(s,dic,k,num)
    print(cost)
    print(''.join(map(str,s)))

'''
思路：遍历0-9每一个数字，计算每一个数字出现k次时候的最小花费
细节：
1.计算过程中使用gap表示距离当前数字i的花费
2.因为要输出具体变化后的结果，所以需要考虑如何变化，如果要变化的值小于当前值，则从前往后替代，如果大于当前值，则从后往前替代（为了保证字典序最小）
'''
from collections import Counter
n,k = map(int, input().split())
s = input()
d = Counter(list(map(int,s)))
res = float("inf")
ans = "A"
for i in range(10):
    tmp_s = s
    need = k - d[i]
    cost = 0
    gap = 1
    while need > 0:
        if i+gap <= 9:
            if d[i+gap] < need:
                tmp_s = tmp_s.replace(str(i + gap), str(i))
                cost += d[i+gap] * gap
                need -= d[i+gap]
            else:
                tmp_s = tmp_s.replace(str(i + gap), str(i), need)
                cost += need * gap
                break
        if i - gap >= 0:
            if d[i-gap] < need:
                tmp_s =tmp_s.replace(str(i-gap), str(i))
                cost += d[i-gap] * gap
                need -= d[i-gap]
            else:
                tmp_s = tmp_s[::-1]
                tmp_s = tmp_s.replace(str(i-gap), str(i), need)
                tmp_s = tmp_s[::-1]
                cost += need * gap
                break
        gap += 1
    if cost < res:
        ans = tmp_s
        res = cost
    elif cost == res and  tmp_s < ans:
        ans = tmp_s
 
print(res)
print(ans)