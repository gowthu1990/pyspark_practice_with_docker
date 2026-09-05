n = int(input("enter a number"))

for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end= "")
    for j in range(2*i,1,-1):
        print("*",end = "")
    
    print()
    