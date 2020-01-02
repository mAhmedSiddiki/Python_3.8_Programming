#square sum - recursion

def sqr_sum(n):
    if n == 1:
        return 1
    else:
        return n*n + sqr_sum(n-1)

a = int(input("Enter a number: "))
b = sqr_sum(a)
print(b)