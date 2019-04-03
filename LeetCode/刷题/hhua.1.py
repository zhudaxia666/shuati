import sys
def jisuan(a):
    if '+' in a:
        return int(a[:a.index('+')])+int(a[a.index('+')+1:])
    elif '-' in a:
        return int(a[:a.index('-')])-int(a[a.index('-')+1:])
    elif '*' in a:
        return int(a[:a.index('*')])*int(a[a.index('*')+1:])
    else:
        return 
a=input()

print(jisuan(a))
