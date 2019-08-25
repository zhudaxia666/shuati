'''
辗转相除法：
1.将两整数求余 a%b = x
2.如果x = 0;则b为最大公约数 
3.如果x != 0,则 a = b；b = x；继续从1开始执行
4.也就是说该循环的是否继续的判断条件就是x是否为0
'''
def gogn(a,b):
    x=a%b
    while x!=0:
        a=b
        b=x
        x=a%b
    return b
print(gogn(12,6))

'''
辗转相减法
1.如果a>b ，a = a - b;
2.如果b>a ，b = b - a;
3.假如a = b ，则 a或b  是最大公约数
4.如果a != b,则继续继续相减，直至a = b
'''
def fun2(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return b
print(fun2(24,12))