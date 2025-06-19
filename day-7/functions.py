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


def is_palindrome(s):
  return s == s[::-1]

# is_palindrome("madam")
print(is_palindrome("whatever"))


def is_palindrome_recursion(s, i,j): # helloworld # madam
  if i>= j:
    return True
  if s[i] != s[j]:
    return False
  return is_palindrome_recursion(s, i + 1, j - 1)


def find_max_iterative(lst):
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

b= find_max_iterative([2,3,4,5,6])
print(b)


def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]

    max_res = find_max_recursive(lst[1:])
    return lst[0] if lst[0] > max_res else max_res

print(find_max_recursive([2,3,4,5,6]))


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