n = int(input("enter a number"))

 def arraySortedOrNot(self, arr, n):
        temp = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > arr[i+1]:
                return False
            else:
                return True
