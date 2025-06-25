def sum_R(n):
    if n == 0:
        return 0
    return n + sum_N(n - 1)

print("Sum using Recursive Method:", sum_N(5))


def sum_I(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print("Sum using Iterative Method:", sum_I(5))