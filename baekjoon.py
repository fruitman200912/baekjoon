n = int(input())
o = [
  [10],
  [1],
  [2,4,8,6],
  [3,9,7,1],
  [4,6],
  [5],
  [6],
  [7,9,3,1],
  [8,4,2,6],
  [9,1]
]
t = []
for i in range(n):
  a, b = map(int,input().split())
  t.append(o[a%10][(b-1)%len(o[a%10])])

for i in range(n):
  print(t[i])