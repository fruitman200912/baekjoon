b = []

for i in range(8):
  b.append(input())

n = 0

for i in range(8):
  for j in range(i%2,8,2):
    if b[i][j] == 'F':
      n+=1

print(n)