from inspect import stack


n = int(input())

pm = []

arr = []
idx = 1

for _ in range(n):

  num = int(input())

  while idx <= num:
    #push
    arr.append(idx)
    pm.append('+')
    idx +=1
  
  if arr[-1] == num:

    arr.pop()
    pm.append('-')

if len(arr) == 0:
  for i in pm:
    print(i)
else:
  print('NO')