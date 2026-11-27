def reverse(arr):
    left = 0
    right = len(arr)-1
    while(left < right):
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1
    return arr

arr = [1,23,45,98,100,61,29]
print(reverse(arr))

#TC :- O(n/2) == O(n)
<<<<<<< HEAD
#SC :- O(1)
=======
#SC :- O(1)    
>>>>>>> 8a41f12 (arrays)
