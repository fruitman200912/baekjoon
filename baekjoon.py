def itin(b, a, i):
  for j in range(a):
    if t != b[j][i]:
      return False
  return True

a = int(input())
b = []

for i in range(a):
  b.append(input())

for i in range(len(b[0])):
  t = b[0][i]
  j = itin(b, a, i)
  if j:
    print(t,end="")
  else:
   print("?",end="")