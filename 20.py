def factorial(n):
  value = 1
  for i in range(1, n+1):
    value *= i
  return value
  

n = factorial(100)
s = str(n)
numberSum = 0
for letter in s:
  a = int(letter)
  numberSum += a

print(numberSum)