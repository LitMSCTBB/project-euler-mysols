'''amicable = []

def d(n):
  divisorSum = 0
  for i in range(1, n):
    if n%i == 0:
      divisorSum += i
  return divisorSum


for i in range (1, 10000):
  if d(d(i)) == i:
    if i not in amicable:
      if i == d(i):
        amicable.append(i)
      else:
        amicable.append(i)
        amicable.append(d(i))

print(amicable)
print(sum(amicable))
this is my code that keeps giving the wrong answer'''

#Credits to jasonbhill for this code. Code found here: http://code.jasonbhill.com/c/project-euler-problem-21/. Nothing was changed except for the time stuff.

def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s
 
def amicable_pairs_xrange(low,high):
    L = [sum_divisors(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs
 
def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])
 

 
ans = sum_pairs(amicable_pairs_xrange(1,10000))

print(ans)

