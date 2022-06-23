from collections import deque
import sys


N = int(input())

arr = deque()

for _ in range(N):

  tmp = sys.stdin.readline().strip()

  if tmp == 'pop':

    if len(arr) == 0:
      print(-1)
      continue

    print(arr.popleft())
  
  elif tmp == 'size':
    print(len(arr))

  elif tmp == 'empty':

    if arr:
      print(0)
    else:
      print(1)
  
  elif tmp == 'front':
    if len(arr) == 0:
      print(-1)
      continue
    print(arr[0])
  
  elif tmp == 'back':
    if len(arr) == 0:
      print(-1)
      continue
    print(arr[-1])

  else:

    n = tmp.split()[1]
    arr.append(n)