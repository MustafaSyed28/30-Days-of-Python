def sum_R(n):
    if n == 0:
        return 0
    return n + sum_R(n - 1)

print("Recursive Sum:", sum_R(5))



def sum_I(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Iterative Sum:", sum_I(3))


