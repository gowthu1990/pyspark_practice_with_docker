n = int(input("enter a number:"))

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    
    print("")