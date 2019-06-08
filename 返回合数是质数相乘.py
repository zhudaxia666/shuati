def f(n):
    result=[]
    i=2
    str1=str(n)+'='
    while n>1:
        if i>0:
            if n % i==0:
                n//=i
                result.append(str(i))
                i-=1
        i+=1
    str1+="*".join(result)
    return str1
if __name__ == "__main__":
    for i in range(100,129):
        print(f(i))