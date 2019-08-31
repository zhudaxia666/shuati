def fun(n,h):
    height=h/2
    sum=100
    
    for _ in range(1,n):
        sum+=height*2
        height=height/2
    print(sum)
    print(height)
fun(1,100)
fun(2,100)
fun(3,100)
fun(10,100)