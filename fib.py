# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recusrsive 
  # base case
  # move towards the base case
  # function calls itself

def slow_fibonacci(n):
  if n <= 1:
    return n
  
  return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print(slow_fibonacci(23))


# use Cace
# Memoizing   Memoizing
# Dynamic Programming
# store our resutls in a dict to look up
cache = {}

def fibonacci(n, total=0):
  if n <= 1:
    return n

  if n not in cache:
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
  
  return cache[n]

print(fibonacci(877))
print(len(cache))