o = input()
x = []

for i in range(len(o)):
  a = int(o[i])
  if a // 4 == 1:
    a-=4
    x.append(1)
  else:
    x.append(0)
  if a // 2 == 1:
    a-=2
    x.append(1)
  else:
    x.append(0)
  x.append(a)

i = 0
while x[i] != 1:
  i+=1
  if i >= len(x):
    print(0)
    break

for i in range(i,len(x)):
  print(x[i],end="")