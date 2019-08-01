'''
将C[]数组的结点序号转化为二进制

1=(001)      C[1]=A[1];

2=(010)      C[2]=A[1]+A[2];

3=(011)      C[3]=A[3];

4=(100)      C[4]=A[1]+A[2]+A[3]+A[4];

5=(101)      C[5]=A[5];

6=(110)      C[6]=A[5]+A[6];

7=(111)      C[7]=A[7];

8=(1000)    C[8]=A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8];

对照式子可以发现  C[i]=A[i-2^k+1]+A[i-2^k+2]+......A[i]; （k为i的二进制中从最低位到高位连续零的长度）例如i=8时，k=3;

可以自行带入验证;

现在引入lowbit(x) 

lowbit(x) 其实就是取出x的最低位1  换言之  lowbit(x)=2^k  k的含义与上面相同 理解一下

下面说代码

int lowbit(int t)
{
return t&(-t);
}
//-t 代表t的负数 计算机中负数使用对应的正数的补码来表示
//例如 :
// t=6（0110） 此时 k=1
//-t=-6=(1001+1)=(1010)
// t&(-t)=(0010)=2=2^1
C[i]=A[i-2^k+1]+A[i-2^k+2]+......A[i];

C[i]=A[i-lowbit(i)+1]+A[i-lowbit(i)+2]+......A[i];

链接：https://blog.csdn.net/Small_Orange_glory/article/details/81290634
'''
'''
区间查询
ok 下面利用C[i]数组，求A数组中前i项的和 
举个例子 i=7;
sum[7]=A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7] ;   前i项和
C[4]=A[1]+A[2]+A[3]+A[4];   C[6]=A[5]+A[6];   C[7]=A[7];
可以推出:   sum[7]=C[4]+C[6]+C[7];
序号写为二进制: sum[(111)]=C[(100)]+C[(110)]+C[(111)];

细细观察二进制 树状数组追其根本就是二进制的应用
'''
def lowbit(x):
    return x&(-x)
def getsum(x,c):
    ans=0
    i=x
    while i>=0:
        ans+=c[i]
        i-=lowbit(i)
        
    return ans

'''
单点更新

当我们修改A[]数组中的某一个值时  应当如何更新C[]数组呢？
回想一下 区间查询的过程，再看一下上文中列出的图


'''
def add(x,y,tree):
    i=x
    while i<len(tree):
        tree[i]+=y
        i+=lowbit(i)
def test(nums):
    n = len(nums)
    sum = [0] * (n+1)
    for i in range(1,n+1):
        sum[i] = sum[i-1] + nums[i-1]
    sum1 = [0] * (n+1)
    for i in range(1,n+1):
        sum1[i] = sum[i] - sum[i-(i&-i)]
    print(sum)
    print(sum1)
a=[1,3,5]
test(a)
        

    