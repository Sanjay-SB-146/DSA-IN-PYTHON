def smallestElement(arr):
    smallest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
        
    return smallest
arr = [32,34,65,4,5,-1,7]
print(smallestElement(arr))

#TC :- O(n)
<<<<<<< HEAD
#SC :- O(1)
=======
#SC :- O(1)
>>>>>>> 8a41f12 (arrays)
