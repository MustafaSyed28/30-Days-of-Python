def fibonacci_iterative(n):
    if n<=0:
      return "n should be gerater than zero"
    elif n ==1 :
      return 0
    elif n==2:
      return 1
    else:
      a, b = 0, 1
      for i in range(2,n):
          a, b = b, a + b
      return b
print(fibonacci_iterative(5))


def fibonacci(n):
    if n<=0:
      return "n should be gerater than zero"
    elif n ==1 :
      return 0
    elif n==2:
      return 1
    else:
      return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))


def reverse_string_recursion(s):
    if len(s) == 0:
        return ""
    return reverse_string_recursion(s[1:]) + s[0]

print(reverse_string_recursion("abc"))