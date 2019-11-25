import math

a=600851475143

def primeCheck(n):
  f = 0
  for k in range(2, math.floor(math.sqrt(n))):
    if n % k == 0:
      f += 1
  if f == 0:
    return True
  else:
    return False



prime_factors = []
for i in range(1, math.floor(a/2) + 1):
  if a % i == 0:
    if primeCheck(i):
      prime_factors.append(i)

print(prime_factors[-1])
