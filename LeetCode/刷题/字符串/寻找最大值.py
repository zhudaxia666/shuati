'''
每行有两个数n,m（n可能是一个很大的整数，但其位数不超过100位，并且保证数据首位非0，m小于整数n的位数）
将n删除m个数，使剩余的
比如当n=92081346718538，m=10时，则新的最大数是9888

'''
n,m=input().split()
l = len(n)
m = int(m)
s=0 
begin = 0 
t = m 
for j in range(l-m):
    maxx = '0'
    for i in range(begin,t+1):
        if maxx<n[i]:
            p=i
            maxx = n[i]
    print(maxx,end='')
    begin = p+1
    t = t+1