def gradient_descent(y):
    x=1
    alpha=0.0001
    deta=1
    count=1
    while abs(deta)>0.00001:
        deta=4*x*(x**2-y)
        x-=alpha*deta
        count+=1
    return x,count
def newton(y):
    x=1
    deta=1
    count=1
    while abs(deta)>0.00001:
        fx=(y-x**2)**2
        deta=4*x*(x**2-y)
        if not deta:
            break
        x-=fx/deta
        count+=1
    return x,count

print(gradient_descent(81))
print(newton(81))
