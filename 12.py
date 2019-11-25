def count_divisors(n):
  num_divisors = 0
  for j in range(1, n+1):
    if n % j == 0:
      num_divisors += 1
  return num_divisors

print(count_divisors())

'''n = 0
i = 1
while True:
  n += i
  if count_divisors(n) > 500:
    print (n)
    break
  i += 1'''