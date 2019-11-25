import math

primes = []
def primeCheck(n):
  f = 0
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      f += 1
  if f == 0:
    return True
  else:
    return False

i = 2
while len(primes) < 10002:
  if primeCheck(i):
    primes.append(i)
  i += 1


print(primes[10000])
