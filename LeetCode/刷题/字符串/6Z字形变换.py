'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

思路：
我们先假定有 numRows=4 行来推导下，其中 2*numRows-2 = 6 , 我们可以假定为 step=2*numRows-2 ，我们先来推导下规则：

第0行： 0 - 6 - 12 - 18
==> 下标间距 6 - 6 - 6 ==> 下标间距 step - step - step

第1行： 1 - 5 - 7 - 11 - 13
==> 下标间距 4 - 2 - 4 - 2 ==> 下标间距step-2*1(行)-2*1(行)-step-2*1(行)-2*1(行)

第2行： 2 - 4 - 8 - 10 - 14
==> 下标间距 2 - 4 - 2 - 4 ==> 下标间距step-2*2(行)-2*2(行)-step-2*2(行)-2*2(行)
第3行：3 - 9 - 15 - 21

==> 下标间距间距 6 - 6 - 6 ==>下标间距step - step - step

可以得出以下结论：
起始下标都是行号
第0层和第numRows-1层的下标间距总是step 。
中间层的下标间距总是step-2*行数，2*行数交替。
下标不能超过len(s)-1

'''
def convert(s,numRows):
    if numRows==1:
        return s
    step=numRows*2-2#间隔
    index=0#记录s的下标
    l=len(s)#
    add=0#真实的间隔
    res=''
    for i in range(numRows):#i表示行号
        index=i
        add=i*2
        while index<l:#产出字符串长度计算下一层
            res+=s[index]#当前行的第一个字母
            add=step-add#第一次间隔是step-2*i,第二次是2*i
            index+=step if i==0 or i==numRows-1 else add
    return res

'''
思路二：
字符串s是以 ZZ 字形为顺序存储的字符串，目标是按行打印。设numRows行字符串分别为 s1，s2,sn，则容易发现，按顺序遍历字符串s时，
每个字符c属于的对应行索引先从s1增加到sn,再从sn减少到s1...如此反复，

算法流程： 按顺序遍历字符串s；
res[i] += c：把每个字符c填入对应行 s_i  ；
i += flag：更新当前字符c对应的行索引；
flag = - flag：在达到 ZZ 字形转折点时，执行反向。
复杂度分析：
时间复杂度 O(N)O(N) ：遍历一遍字符串s；
空间复杂度 O(N)O(N) ：各行字符串共占用 O(N)O(N) 额外空间。

作者：jyd
链接：https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
def converse(s,numRows):
    if numRows<2:
        return s
    res=['' for _ in range(numRows)]
    i,flag=0,-1
    for c in s:
        res[i]+=c
        if i==0 or i==numRows-1:
            flag=-flag
            i+=flag
    return ''.join(res)