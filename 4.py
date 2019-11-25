def largest_element(list_select):
  l = list_select[0]
  for i in range(1, len(list_select)):
    if list_select[i] > l:
      l = list_select[i]
  return l    


palindrome_products = []

for a in range(100, 1000):
  for b in range(100, 1000):
    x=a*b
    s=str(x)
    s_2=s[::-1]
    if s == s_2:
      palindrome_products.append(x)


print(largest_element(palindrome_products))