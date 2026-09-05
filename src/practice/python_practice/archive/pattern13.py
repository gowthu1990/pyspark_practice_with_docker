n = int(input("enter a number"))

counter = 0

for i in range(1,n+1):
    for j in range(0,i):
        counter = counter +1
        print(counter,end = " ")
    print()