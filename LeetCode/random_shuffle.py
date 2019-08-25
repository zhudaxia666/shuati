import random
def shuffle(l):
    tmp=list()
    for i in range(0,len(l)):
        if len(l)!=0:
            r=random.randint(0,len(l)-1)
            tmp.append(l[r])
            l.remove(l[r])
        else:
            break
    return tmp