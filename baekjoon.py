n = int(input())

key = n if n >= 10 else n*10

a = key//10
b = key%10

count = 0

while(1):
  c = b
  n = ((a+b)%10) + c*10
  a = n//10
  b = n%10
  count+=1
  if key == n:
    break

print(count)