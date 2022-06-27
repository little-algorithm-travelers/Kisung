import sys

N = int(input())

arr = []

for _ in range(N):

  tmp =  sys.stdin.readline().strip()

  if tmp == 'pop':

    if arr:
      print(arr.pop())
    else:
      print(-1)


  elif tmp == 'size':
    print(len(arr))


  elif tmp == 'empty':
    if not arr:
      print(1)
    else:
      print(0)


  elif tmp == 'top':
    if arr:
      print(arr[-1])
    else:
      print(-1)


  else:

    n = tmp.split()

    
    arr.append(n[1])