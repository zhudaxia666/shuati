n = int(input())
data = [int(x) for x in input().split()]
dp = [1 for _ in range(len(data)+1)]
for i in data:
    if i==1:
        dp.pop(0)
        for j in range(len(dp)-2,-1,-1):
            dp[j]+=dp[j+1]
        print('1:',dp)
    else:
        dp.pop()
        for j in range(1,len(dp)):
            dp[j]+=dp[j-1]
        print('0:',dp)
mo = 1000000007
print(dp[0]%mo)