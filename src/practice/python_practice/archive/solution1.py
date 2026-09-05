str = input("enter a number")
    
def largest_Odd_Number(str):
    if(len(str) > 0):
        for idx, ch in enumerate(str[::-1]):
            if(int(ch) % 2 != 0):
                return str[:len(str)-idx]
    else:
        return "" 

print(largest_Odd_Number(str)) 