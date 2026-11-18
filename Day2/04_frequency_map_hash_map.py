nums = [1,2,3,4,5,2,3,4,1,6,8,2,1]
# Method 1
'''
freq_map = {}
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)

'''

# Method 2

hash_map = {}
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)