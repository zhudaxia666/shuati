def getIndexof(str1,str2):
    if not str1 or not str2 or len(str2)<1 or len(str1)<len(str2):
        return -1
    s1=0
    s2=0
    next_arr=getNextArray(str2)
    while s1<len(str1) and s2<len(str2):
        if str1[s1]==str2[s2]:#str1和str2对应字符相同，同时加加
            s1+=1
            s2+=1
        elif next_arr[s2]==-1:
            s1+=1#不相同，next[mi] == -1表示str2调到第一个位置，此时说明str1对应位置与str2的第一个位置不用，则str1对应位置加1 
        else:
            s2=next_arr[s2]
    return True if s2==len(str2) else False
def getNextArray(str2):
    if len(str2)==1:
        return [-1]
    next_arr=[0]*len(str2)
    next_arr[0]=-1
    next_arr[1]=0
    pos=2#来到的位置
    cn=0#跳到的位置
    while pos<len(next_arr):
        if str2[pos-1]==str2[cn]:
            cn+=1
            next_arr[pos]=cn
            pos+=1
        elif cn>0:
            cn=next_arr[cn]
        else:
            next_arr[pos]=0
            pos+=1
    return next_arr
if __name__ == "__main__":
    str1="abcabcababdccc"
    str2="ababa"
    print(getIndexof(str1,str2))
