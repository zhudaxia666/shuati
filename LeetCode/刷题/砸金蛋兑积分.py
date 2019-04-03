import sys
l=sys.stdin.readline().strip()
l=list(map(int,l.split()))
def dui(l):
    if l==[]:
        return 0
    if len(l)==1:
        return l[0]
    s=0
    while len(l)!=0:
        if len(l)==3:
            i=1
        else:
            i=l.index(min(l))
        if (i-1)==-1 and (i+1)==len(l):
            s+=l[i]
        elif (i-1)==-1 and (i+1)<len(l):
            s+=l[i]*l[i+1]
        elif (i-1)>-1 and (i+1)==len(l):
            s+=l[i-1]*l[i]
        else:
            s+=l[i-1]*l[i]*l[i+1]
        l.pop(i)
    return s
print(dui(l))
        




    
        


    
