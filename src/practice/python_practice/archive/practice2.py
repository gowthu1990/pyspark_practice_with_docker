str = " I love India"

rev = ""

for i in str:
    print(i)

for i in range(len(str)-1,0,-1):
    rev = rev + str[i]

print(rev)