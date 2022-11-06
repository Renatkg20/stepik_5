import random
user = "1 2 3 4"

l = user.split(" ")


def shufl(w):
    r = []
    r.append(w[-1])
    l.pop(-1)
    
    w.append(r[0])
    return " ".join(w)

def shufl1(w):
    random.shuffle(w[:-1])
    return " ".join(w)

"""
if len(l) % 2 ==0:
    r = l[:-1]
    print(r)
    for i in range(len(r)):
        if i % 2 == 0:
            n.append(l[i])
        else: 
            n.append(l[i])
    n.append(l[-1])
else:
    for q in range(len(l)):
        if q % 2 == 0:
            n.append(l[q])
        else:
           n.append(l[q])

print(" ".join(n))

"""

def odd(w):
    n = []
    r = w[:-1]
    for i in range(len(r)):
        if i % 2 == 0:
            w[i]
            n.insert(i+1, w[i])
        else: 
            n.insert(i-1, w[i])
    n.append(w[-1])
    return " ".join(n)


def even(w):
    n = []
    r = w
    for i in range(len(r)):
        if i % 2 == 0:
            w[i]
            n.insert(i+1, w[i])
        else: 
            n.insert(i-1, w[i])
    return " ".join(n)

if len(l) % 2 != 0:
    print(odd(l))
else:
    print(even(l))

