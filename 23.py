def d(n):
  divisorSum = 0
  for i in range(1, n):
    if n%i == 0:
      divisorSum += i
  return divisorSum

abundant = []

for i in range(28124):
  if d(i) > i:
    abundant.append(i)

abundantSums = []

for i in range(len(abundant)):
  for j in range(i, len(abundant)):
    if abundant[i] + abundant[j] not in abundantSums:
      abundantSums.append(abundant[i] + abundant[j])

print(28123 - len(abundantSums))