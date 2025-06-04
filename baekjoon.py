n = int(input())
ns = [0 for _ in range(n)]

ns_c = input().split()

for i in range(n):
  ns[i] = int(ns_c[i])


a = 1
while True:
  t = False
  a+=1
  for i in ns:
    if a <= i and a % i != 0:
      for j in range(2,a):
        if a % j == 0:
          if not j in ns:
            t = True
  if t:
    continue
  break

print(a)