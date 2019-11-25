desired = []
for a in range(10, 100):
  for b in range(a+1, 100):
    sa = str(a)
    sb = str(b)
    if sa[0] == sb[0] and "0" not in sa and "0" not in sb:
      if int(sa[1])/int(sb[1]) == a/b:
        desired.append((a, b))
    elif sa[1] == sb[0] and "0" not in sa and "0" not in sb:
      if int(sa[0])/int(sb[1]) == a/b:
        desired.append((a, b))
    elif sa[0] == sb[1] and "0" not in sa and "0" not in sb:
      if int(sa[1])/int(sb[0]) == a/b:
        desired.append((a, b))
    elif sa[1] == sb[1] and "0" not in sa and "0" not in sb:
      if int(sa[0])/int(sb[0]) == a/b:
        desired.append((a, b))

print(desired)