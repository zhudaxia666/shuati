'''
找出字符串最长回文子串，暴力解法：在字符串两边和任意两个字符间插入一个特定的字符'#',然后分别以每个字符为中心，统计最长回文串，最后除以2就得出最长回文子串长度。
可以使时间复杂度为O(n)
首先还是“中心扩散法”的思想：回文串可分为奇数回文串和偶数回文串，它们的区别是：奇数回文串关于它的“中点”满足“中心对称”
偶数回文串关于它“中间的两个点”满足“中心对称”。为了避免对于回文串字符个数为奇数还是偶数的套路。首先对原始字符串进行预处理，
方法也很简单：添加分隔符。

链接：https://leetcode-cn.com/problems/two-sum/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/


概念：
1）回文直径：以某字符为中心，回文的长度,建立一个回文半径数组，每个元素表示以该元素为中心的回文半径
2）最右回文右边界R，回文子串最右边的位置
3）回文右边界的中心c（和2）半生的）

两种可能性：第一种：i在R（回文右边界）的外部，暴力扩

第二种：i在R的内部，这有分三种情况
1）i'（关于c的对称点）回文半径彻底在L和R里面。i的回文半径直接确定，等于i'的距离，时间复杂度为O(1)
2）i'回文半径彻底在L和R的外边。 i的回文半径直接确定，等于i和R的距离，时间复杂度为O(1)
3）i'回文半径和L压线，i到R这段不用验证，但能不能向右扩的很大，需要自己去验证
eg:
给你一个字符串，在后添加若干字符，是整个字符串是回文串且最短
'''
def manache(str1):
    n=len(str1)
    res=[0]*(2*n+1)
    index=0
    for i in range(len(res)):
        if (i & 1)==0:
            res[i]='#'  
        else:
            res[i]=str1[index]
            index+=1
    return res

def maxlcp(str1):
    if not str1 or len(str1)==0:
        return ''
    char=manache(str1)
    p=[0]*len(char)#回文半径数组
    c=-1#回文中心
    R=-1#右边界
    m=-float('inf')
    t=-1
    for i in range(len(char)):
        #当 p[j] 的范围很小的时候，有 p[i] = p[j]，p[i] 的值再大不过超过 R - i 
        #当 i >= mx 的时候，此时也只能老老实实使用“中心扩散法”来逐渐得到 p 数组的值，同时记录 id 和 mx
        p[i]=min(p[2*c-i],R-i) if R>i else 1
        while i+p[i]<len(char) and i-p[i]>=0:#验证的区域没越界和左边区域没越界，对应四种情况
            if char[i+p[i]]==char[i-p[i]]:#扩出来的两部分相同，回文半径加1
                p[i]+=1
            else:
                break
        if i+p[i]>R:#统计回文半径，即扩充的区域超过了R，就有了一个新的右边界，更新R和C
            R=i+p[i]
            c=i
        if m<p[i]:#记录全局最大值
            m=p[i]
            t=i
    print(char)
    print(p)
    return ''.join(char[t-p[t]+1:t+p[t]]).replace('#','')

a='abc1234321ab'
print(maxlcp(a))