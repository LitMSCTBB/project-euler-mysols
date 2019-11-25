fibonacci = [1, 1]
while True:
  fibonacci.append(fibonacci[-1] + fibonacci[-2])
  last_fib = str(fibonacci[-1])
  if len(last_fib) == 1000:
    print (len(fibonacci))
    break