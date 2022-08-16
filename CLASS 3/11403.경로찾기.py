

from collections import deque




N = int(input())

arr = []

for _ in range(N):

  arr.append(list(map(int, input().split())))

res = [[ 0 for _ in range(N)] for _ in range(N)]



def bfs(i):

  Q = deque()


  for j in range(N):

    if arr[i][j] == 1:
      Q.append([i,j])
    
  
  while len(Q) > 0:

    tmp1, tmp2 = Q.popleft()
    res[i][tmp2] = 1

    for k in range(N):

      if arr[tmp2][k] == 1 and res[i][k] == 0:
        Q.append([tmp2,k])

for i in range(N):
  bfs(i)

for i in res:
  print(*i)