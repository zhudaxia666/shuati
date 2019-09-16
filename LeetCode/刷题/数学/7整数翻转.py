'''
设当前计算结果为ans，下一位为pop

从ans*10+pop>MAx_value这个溢出条件来看
当出现ans>Max_value/10且还有pop需要添加时，则一定溢出
当出现ans==Max_value/10且pop>7时。则一定溢出，7是2^31-1的个位数

从ans*10+pop<Min_value这个溢出条件来看
当出现ans<Min_value/10且还有pop需要添加时，则一定溢出
当出现ans==Max_value/10且pop<-8时。则一定溢出，7是-2^31的个位数

Python： 存储数字理论上是无限长度，因此每次计算完后判断res与of的大小关系即可；
Java： 数字计算会溢出，因此要判断res和of / 10的大小关系（即确定再添 11 位是否会溢出）。
Python的坑： 由于Python的 // 操作是向下取整，导致正负数取余 % 操作结果不一致，因此需要将原数字转为正数操作。

'''
def reverse(x):
    y,res=abs(x),0
    of=(1<<31)-1 if x>0 else 1<<31
    while y!=0:
        res=res*10+y%10
        if res>of:
            return 0
        y//=10
    return res if x>0 else -res

print(reverse(-123))
        

    
