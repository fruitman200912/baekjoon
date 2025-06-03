n = int(input())
f = int(input())

for i in range(100):
  n = n - (n%100) + i
  if n != 0 and n%f == 0:
    break

print("%02d"%(n%100))