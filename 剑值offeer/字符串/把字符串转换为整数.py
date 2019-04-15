'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
实例：
输入
+2147483647
    1a33
输出
2147483647
    0

思路：
对于这个题目，需要注意的要点有：

指针是否为空指针以及字符串是否为空字符串；
字符串对于正负号的处理；
输入值是否为合法值，即小于等于'9'，大于等于'0'；
int为32位，需要判断是否溢出；
使用错误标志，区分合法值0和非法值0。
'''
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        else:
            minus=False#是否为负数
            flag=False#符号位判断
            if s[0]=='+':
                flag=True
            if s[0]=='-':
                flag=True
                minus=True
            begin=0
            if flag:
                begin=1
            num=0
            minus=-1 if minus else 1
            for each in s[begin:]:
                if each>='0' and each<='9':
                    num=num*10+minus*(ord(each)-ord('0'))
                else:
                    num=0
                    break
            return num