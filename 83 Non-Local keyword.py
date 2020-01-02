#nonlocal

def f():
    x = 5
    def g():
        nonlocal x
        x = 8
    g()
    print("x = ",x)

f()