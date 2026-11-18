def check_palindrome(n):
    num = n
    result = 0
    while n>0:
        ld = n % 10
        result = (result*10)+ld
        n = n // 10
    if(result == num):
        print("The number is palindrome")
    else:
        print("The Number is not a Palindrome")
check_palindrome(123321)

#TC :- O(log10(N))
#SC :- O(1)