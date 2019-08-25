''''
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
思路：
这题说了一堆，提取主要信息，我们不难整理出，满足如下条件才可以认为是顺子：

输入数据个数为5；
输入数据都在0-13之间；
没有相同的数字；
最大值与最小值的差值不大于5。
PS：大小王可以当成任意数。

这里可以使用一个技巧，即利用一个flag记录每个数字出现的次数
'''
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers)<5:
            return False
        min_num=14
        max_num=-1
        flag=0
        for number in numbers:
            if number<0 or number>13:
                return False
            #大小王可以模拟任何数
            if number==0:
                continue
            #如果数字出现一次
            if (flag >> number) & 1==1:
                return False
            #按位保存数组出现的次数，比如0110表示，0出现0次，1出现1次，2出现1次3出现0次
            flag |=1 << number
            #更新最小值
            if number<min_num:
                min_num=number
            #更新最大值
            if number>max_num:
                max_num=number
            #超过范围一定不是顺子
            if max_num-min_num>=5:
                return False
        return True
'''
本题思路很好想，相信玩过QQ斗地主的人都知道什么叫赖子牌，本题实际是一个意思。所谓顺子只需要判断两点：1、五张牌没有重复 2、王牌个数等于顺子中空缺的位置。
'''
def IsContinuous(number):
    if len(number)==0:
        return False
    #对数组排序
    number.sort()
    #统计大小王个数
    num=number.count(0)
    numflack=0#间隔数
    for i in range(num,len(number)-1):
        if number[i]==number[i+1]:#如果有对子，肯定不会是
            return False
        if number[i+1]==number[i]+1:
            continue
        else:
            #统计相邻数字间的空缺数
            numflack+=(number[i+1]-number[i]-1)
    if numflack<=num:
        return True
    else:
        return False
        

        
        