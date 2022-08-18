from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

line = [[] for _ in range(N+1)]

for i in range(M):

  u,v = map(int, sys.stdin.readline().rstrip().split())

  line[u].append(v)
  line[v].append(u)

v = [False for _ in range(N+1)]

Q = deque()

res = 0

for i in range(1, N+1):

  if v[i]:
    continue

  res += 1

  Q.append(i)

  while len(Q) >0:

    tmp = Q.popleft()

    v[tmp] = True

    for j in line[tmp]:
      if not v[j]:
        Q.append(j)
        v[j] = True

print(res)
  
  