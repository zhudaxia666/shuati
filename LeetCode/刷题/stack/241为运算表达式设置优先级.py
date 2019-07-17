'''
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:
输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
示例 2:
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''
'''
# 相当于是根据所给式子构造运算二叉树的问题，
# 所以每次遍历其中的每个运算符作为根结点，
# 该运算符前后的内容分别递归得到左右子树可能的构造，每种左右子树组合得到一种构造结果
'''
def diffwaystoCompute(input):
    nums=[]
    ops=[]
    num=''
    #获得数字列表和运算符列表，也可以不这么做直接递归处理字符串
    for i in input:
        if i in ['+','-','*']:
            nums.append(int(num))
            ops.append(i)
            num=''
        else:
            num+=i
    nums.append(int(num))
    #递归运算
    def calc(nums,ops):
        if not ops:
            return [nums[0]]
        if len(ops)==1:
            if ops[0]=='+':
                return [nums[0]+nums[1]]
            elif ops[0]=='-':
                return [nums[0]-nums[1]]
            else:
                return [nums[0]*nums[1]]
        res=[]
        for i in range(len(ops)):
            for num1 in calc(nums[:i+1],ops[:i]):
                for num2 in calc(nums[i+1:],ops[i+1:]):
                    res.append(calc([num1,num2],[ops[i]])[0])
        return res
    return calc