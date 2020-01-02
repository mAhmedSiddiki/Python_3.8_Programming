#for loop break and continue

p=[1,2,3,4,5,6,7,8,9,10]

print("Break Statement")
for i in p:
    if i == 4:
        print("stop")
        break
    print(i)

print("\nContinue Statement")
for i in p:
    if i == 4:
        print("skip")
        continue
    print(i)