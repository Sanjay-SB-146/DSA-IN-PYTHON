# 1st Method Brute Force Approach
'''
def print_factors(n):
    result = []
    for i in range(1,n+1):
        if(n%i==0):
            result.append(i)
    print(result)
print_factors(100)
'''
# TC :- O(N)
# SC :- O(K) k is len of result

# 2nd Method Better Solution
'''
def check_factors(n):
    result = []
    for i in range(1,(n//2)+1):
        if(n%i==0):
            result.append(i)
    result.append(n)
    print(result)
check_factors(100)
'''

# TC :- O(N/2) = similar to O(N)
# SC :- O(K)

# 3rd Optimal Solution
'''
for example 36 loop squrt thak
    1 --> 36
    2 --> 18
    3 --> 12
    4 --> 9
    6 --> 6 
append both but in last append only one '''
from math import sqrt
def check_factors(n):
    result = []
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            result.append(i)
            if(n//i != i):
               result.append(n//i)
    result.sort()
    print(result)
check_factors(100)

# if they ask sort use result.sort()

# TC :- O(sqrt(N))
# SC :- O(K)