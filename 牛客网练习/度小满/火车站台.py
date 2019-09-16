'''
在Z省，有若干个个城市坐落在一条直线上，从左到右依次标号1,2,3,…，其中每个城市有一个火车站点，
现今已经开放了n条火车路线，第i条火车路线是从第Yi个城市到第Xi个城市，因为Z省地势奇特，标号小的城市地势较低，
所以火车是从高往低开的，再通过神秘力量传送回高地，即Yi一定大于Xi，它在沿途的所有城市都会停靠
（显然不包括起点Yi，但是包括终点Xi），火车停靠就需要火车站台来运营维护。火车站台随着运营线路的数量不同，
其损耗速度、维护成本也各异，现在我们想知道所有站台中，所运营的线路数最大是多少。
'''
n=int(input())
route=[]
for i in range(n):
    route.append([int(i) for i in input().split()])
dp=[0 for _ in range(100001)]
for each in route:
    dp[each[0]]+=1
    dp[each[1]]-=1
count=0
max_num=0
for i in dp:
    count+=i
    max_num=max(max_num,count)
print(max_num)
