import math

primes = [2]
def primeCheck(n):
  f = 0
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      f += 1
  if f == 0:
    return True
  else:
    return False

i = 3
while True:
  if primes[-1] < 2000000:
    if primeCheck(i):
      primes.append(i)
    i += 1
  else:
    break


print(sum(primes))