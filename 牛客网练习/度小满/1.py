s=input()
res=[0]*len(s)
begin=0
s=list(s)
n=len(s)
index=0
while begin<n:
    index=begin+s[begin:].index('L')
    if index!=len(s)-1 and s[index+1]=='R':
        if (index-begin+1)%2==0:
            res[index]=(index-begin+1)//2
            res[index-1]=(index-begin+1)//2
        else:
            res[index]=index-begin
            res[index-1]=index-begin-1
    elif index==len(s)-1:
        if (index-begin+1)%2==0:
                res[index]=(index-begin+1)//2
                res[index-1]=(index-begin+1)//2
        else:
            res[index]=(index-begin+1)//2+1
            res[index-1]=(index-begin+1)//2
        break
    elif index!=len(s)-1 and s[index+1]=='L':
        if 'R' in s[index+1:]:
            tmp=s[index+1:].index('R')
            res[index]+=tmp-index-1
            if (index-begin+1)%2==0:
                res[index]+=(index-begin+1)//2
                res[index-1]+=(index-begin+1)//2
            else:
                res[index]+=index-begin
                res[index-1]+=index-begin-1
            index=tmp-1
        else:
            res[index]+=n-index-1
            if (index-begin+1)%2==0:
                res[index]+=(index-begin+1)//2
                res[index-1]+=(index-begin+1)//2
            else:
                res[index]+=index-begin
                res[index-1]+=index-begin-1
            break
            
    begin=index+1
for i in res:
    print(i,end=' ')