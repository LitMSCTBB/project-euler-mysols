
fibonacci = [1, 2]
fibSum = 0

def add_term_fibonacci():
  fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])
  return fibonacci

while fibonacci[len(fibonacci) - 1] <= 4000000:
  add_term_fibonacci()


for i in range(len(fibonacci)):
  if fibonacci[i] % 2 == 0:
    fibSum += fibonacci[i]

print(fibSum)