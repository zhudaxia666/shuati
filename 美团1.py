'''
小明家有一些彩球，一段时间后小明玩耍时将它们无序的散落在家中，一天，小明想对其进行整理，
规则为一个篮子中只放一种颜色彩球，可有多个篮子放同一颜色的球，每个篮子里的球不少于2个。
假设小明整理好后，能使各篮子中彩球数量是相同的，则认为小明整理好了。用一个数字表示一种颜色彩球，
一组数表示小明已经找到了的彩球，问小明用找到的全部彩球能按规则整理好么？
'''
def qiu(n,a):
    if n!=len(a) or n%2==1:
        return 0
    dic={}
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    flag=0
    tem=[]
    num=0
    for key in dic.keys():
        tem.append(dic[key])
        if dic[key]<2:
            return 0
    if len(list(set(tem)))==1:
        return len(tem)
    else:
        
        m=tem.pop(tem.index(min(tem)))
        for i in tem:
            if i % m!=0:
                flag=1
            else:
                num+=i//m
    if flag==1:
        return 0
    else:
        return num+1
n=int(input())
a=list(map(int,input().split()))
print(qiu(n,a))