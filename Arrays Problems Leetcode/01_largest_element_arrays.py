def largestElement(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>largest):
            largest = arr[i]
    return largest

arr = [10,5,8,24,76,1,2,3]
print(largestElement(arr))

#TC :- O(n)
<<<<<<< HEAD
#SC :- O(1)
=======
#SC :- O(1)
>>>>>>> 8a41f12 (arrays)
