import sys
lines=sys.stdin.readline().strip()
line1=list(map(int,lines.split()))
lines=sys.stdin.readline().strip()
line2=list(map(int,lines.split()))
def tan(line1,line2):
    n,m=line1[0],line1[1]
    if len(line2)==0:
        return 0
    if len(line2)==1:
        return 1
    sorted(line2)
    count=0
    while n>0:
        if n>=2:
            if line2[n-1]+line2[n-2]<m:
                count+=1
            else:
                count+=2
            line2.pop(n-1)
            line2.pop(n-2)
            n-=2
        else:
            count+=1
            line2.pop()
    return count
print(tan(line1,line2))
    
        
                



