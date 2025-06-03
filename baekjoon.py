n = int(input())
f = int(input())

for i in range(100):
  if f < 11 and f == 0:
    continue
  if n%f == 0:
    break
  f = f - (f%100) + i

print("%02d"%(f%100))