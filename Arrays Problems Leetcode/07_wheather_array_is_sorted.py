def isSorted(nums):
    srt = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            srt = False
    return srt
nums = [1,2,3,3,4,4,5]

print(isSorted(nums))
