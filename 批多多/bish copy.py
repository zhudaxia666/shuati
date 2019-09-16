s=int(input())
for i in range(s):
    a=list(input())
    a.sort()
    b=list(input())
    b.sort()
    if (len(a)==len(b) and a!=b) or len(a)<len(b):
        print('{')
        print('}')
    else:
        print('{')
        for i in range(len(a)):
            print('l',end=' ')
        print()
        print('}')
        