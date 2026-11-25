def secondLargest(arr):
    largest = 0
    second = 0
    for num in arr:
        if num>largest:
            second = largest
            largest = num
        elif num> second and num != largest:
            second = num
    return second

arr = [1,2,3,43,25,76,67]
print(secondLargest(arr))

#TC :- O(n)
#SC :- O(1)
