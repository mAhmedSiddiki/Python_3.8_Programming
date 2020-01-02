#function forwarding
def add(p,q,r):
    return p+q+r

def add2(q,p,r):
    return p+q+r

def correction(p,q,r):
    return add2(q,p,r)

d = [1000,20,10]
print(add(d[0],d[1],d[2]))
print(correction(*d))