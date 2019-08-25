'''
看了大家的解法，前缀树的确可以通过Node来做，但是这是一个效率并不高的做法。python的字典可以很好实现
插入apple-->等价于-->实现{a:{p:{p:{l:{e:{}}}}}}
同时，插入apple 和 app都需要一个标记一个单词的末端 -->等价于-->实现{a:{p:{p:{'99999':1,l:{e:{'99999':1}}}}}}

为什么用99999？首先题目输入a-z，插入的99999是绝对不会影响值和深度的，其次，我喜欢99999😄

代码： 
'''
class Trie:
    def __init__(self):
    """
    Initialize your data structure here.
    """
        self.dic = {}

    def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
        dic_todo = self.dic
        for i in word:
            if i in dic_todo:
                dic_todo = dic_todo[i]
            else:
                dic_todo[i] = {}
                dic_todo = dic_todo[i]
        dic_todo['99999'] = 1

    def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
        dic_todo = self.dic
        for i in word:
            if i in dic_todo:
                dic_todo = dic_todo[i]
            else:
                return False
        if '99999' in dic_todo:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
        dic_todo = self.dic
        for i in prefix:
            if i in dic_todo:
                dic_todo = dic_todo[i]
            else:
                return False
        return True