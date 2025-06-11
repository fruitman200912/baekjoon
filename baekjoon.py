n = list(map(int,input().split()))

i = 2
while 1:
  count = 0
  for j in n:
    if i % j ==0:
      count += 1
  if count>=3:
    break
  i+=1

print(i)