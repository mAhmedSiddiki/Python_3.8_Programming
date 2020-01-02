# fibonacci serise print

def fibonacci(n):
    first = 0
    second = 1

    print(first)
    print(second)

    i=3
    while i<=n:
        fibo = first+second
        print(fibo)
        first = second
        second = fibo
        i = i+1

a = int(input("Enter a number: "))
fibonacci(a)