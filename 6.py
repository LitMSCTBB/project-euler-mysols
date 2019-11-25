square_sum = 0
for i in range(1, 101):
  square_sum += i*i

normal_sum = 0
for j in range(1, 101):
  normal_sum += j

print (normal_sum ** 2 - square_sum)