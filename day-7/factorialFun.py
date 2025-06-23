# functions
 
def factorial(n):
    if n == 0 | n ==1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(5))


