# 链接：https://www.nowcoder.com/questionTerminal/ce9d7cdac6e34e42919e787a8baf8a2b
# 来源：牛客网
'''
作者：zehong
链接：https://www.nowcoder.com/questionTerminal/ce9d7cdac6e34e42919e787a8baf8a2b
来源：牛客网

deal起到标记作用，用来标记手上是否有商品，如果当前国家的价格比上一个国家价格高，并且我手上没有商品，
就把上一次国家的商品买到手，并作为一次交易次数和计算累积差价。如果当前国家的价格比上一个国家的低， 
说明我们在上一个国家应该出手手上的商品，不然会亏钱，同时将deal标记为0。cnt表示截至当前国家交易次数。
'''
n = int(input())
num = list(map(int, input().split()))
deal = 0
profit = 0
cnt = 0
for i in range(1,n):
    if num[i] > num[i-1]:
        profit += num[i]-num[i-1]
        if deal == 0:
            cnt += 1
        deal = 1
    if num[i] < num[i-1]:
        cnt += deal
        deal = 0
print(profit,cnt+deal)