n = int(input("enter a number"))

for i in range(1,n+1):
    for j in range(0,i):
        print(j+1,end="")
    for m in range(0,2 * n - (2 * i - 1)):
            print(" ",end = "")
    for k in range(i,0,-1):
        print(k,end="")
    print()