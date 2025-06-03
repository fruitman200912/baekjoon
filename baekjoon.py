n = int(input())
f = int(input())

while n % f != 0:
  n+=1

print("%02d"%(n%100))