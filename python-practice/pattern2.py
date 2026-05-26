n = int(input("enter a number:"))

for i in range(n):
    for j in range(i):
        print("*", end="")
    print("")