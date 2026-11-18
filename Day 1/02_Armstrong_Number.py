# ArmStrong Number = 153 = 1^3+5^3+3^3
#                        = 153 then armstrong

def Check_Armstrong(n):
    num = n
    num_of_digit = 0
    while n>0:
        ld = n % 10
        num_of_digit += 1
        n = n // 10
    print(f"The Number of Digits are : {num_of_digit}")

    n = num
    total = 0
    while num > 0:
        last_digit = num % 10
        total = total + (last_digit**num_of_digit)
        num = num // 10
    if(n == total):
        print("The Number is Armstrong Number")
    else:
        print("Not Armstrong Number")

    
Check_Armstrong(1634)