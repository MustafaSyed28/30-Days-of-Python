def count_digit_R(n):
    if n == 0:
        return 0
    return 1 + count_digit_R(n // 10)

print("Recursive Digit Count:", count_digit_R(24567))



def count_digit_I(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

print("Iterative Digit Count:", count_digit_I(112300))
