''''
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。
（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）
给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， 
answer[i] 才为 true，否则为 false。
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
'''
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        ans = []
        for q in queries:
            index = 0
            flag = True
            #遍历queries中的每一个字符串，如果字符串中出现大写字符，但在pattern中没有出现，就返回false
            for p in pattern:
                while index < len(q):
                    if q[index] == p:#当前位置字符相同就退出循环，继续patter得下一个字符
                        break
                    if q[index].isupper() and q[index] != p:
                        flag = False
                        break
                    index += 1
                if index >= len(q) or (not flag):
                    flag = False
                    break
                index += 1
            #当遍历完patter后还剩余，判断剩余部分是否出现大写字母
            while index < len(q):
                if q[index].isupper():
                    flag = False
                    break
                index += 1
            ans.append(flag)
        return ans
