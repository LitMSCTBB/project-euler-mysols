pset = []
def truncate_right(k, n):
  string_n = str(n)
  new_string_n = string_n[0:len(string_n) - k]
  return int(new_string_n)

def truncate_left(k, n):
  string_n = str(n)
  new_string_n = string_n[k:len(string_n)]
  return int(new_string_n)

def num_digits(n):
  string_n = str(n)
  return len(string_n)

def isPrime(n):
  f = 0
  for i in range(2, n):
    if n % i == 0:
      f += 1
  if f == 0:
    return True
  else:
    return False

n = 11
while len(pset) < 11:
  if isPrime(n):
    check = 0
    for j in range(1, num_digits(n)):
      if isPrime(truncate_left(j, n)):
        check += 1
    for m in range(1, num_digits(n)):
      if isPrime(truncate_right(m, n)):
        check += 1
    if check == 2*(num_digits(n) - 1):
      pset.append(n)
  n += 1

print(pset, sum(pset))