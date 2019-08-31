'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''
def isValid(s):
        stack = []
        lookup = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for alp in s:
            if alp in lookup:
                stack.append(alp)
                continue
            if stack and lookup[stack[-1]] == alp:
                stack.pop()
            else:
                return False
        return True if not stack else False