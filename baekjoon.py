n = int(input())
n_list = list(map(int,input().split()))

num = max(n_list)+1
while 1:
  for i in n_list:
    if num % i != 0:
      break
    else:
      for i in range(2,num):
        if num % i == 0 and not(i in n_list):
          break
  else:
    break
  num += 1

print(num)