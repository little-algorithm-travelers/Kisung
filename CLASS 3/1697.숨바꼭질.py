from collections import deque


arr = [0 for _ in range(100001)]

N, K = map(int, input().split())

if N == K:
  print(0)
else:

  q = deque()

  q.append(N)
  v = True

  while v:
    tmp = q.popleft()

    for i in (tmp-1,tmp+1, tmp*2):
      
      if i > 100000 or i < 0:
        continue
      if arr[i] != 0:
        continue
      arr[i] = arr[tmp]+1
      if i == K:
        v = False;


      q.append(i)


  print(arr[K])

