a = {1:2,"apple":4,5:6}
b = input()

if b in a:
    print(b,' = ',a[b])
else:
    print('There is no',b,'item')



if b not in a:
    print('There is no',b,'item')
else:
    print(b,' = ',a[b])