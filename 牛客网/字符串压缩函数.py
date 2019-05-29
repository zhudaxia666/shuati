'''
输入一串字符，请编写一个字符串压缩程序，将字符串中连续出现的重复字母进行压缩，并输出压缩后的字符串。
例如：
aac 压缩为 1ac
xxxxyyyyyyzbbb 压缩为 3x5yz2b
'''
def countstr(s):
    if not s or s==" ":
        return s
    s1=''
    i=0
    while i<len(s):
        count=0
        for j in range(i+1,len(s),1):
            if s[j]==s[i]:
                count+=1
            else:
                break
        if count>0:
            s1+=str(count)+s[i]
        else:
            s1+=s[i]
        i+=count+1
    return s1
s=input()
print(countstr(s))