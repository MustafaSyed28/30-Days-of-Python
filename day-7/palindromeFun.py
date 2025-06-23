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





