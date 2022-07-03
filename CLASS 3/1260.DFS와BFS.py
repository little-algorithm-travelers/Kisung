from collections import deque


N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]

visited = [False for _ in range(N+1)]

for _ in range(M):
  tmp = list(map(int, input().split()))
  
  arr[tmp[0]].append(tmp[1])
  arr[tmp[1]].append(tmp[0])

for ar in arr:
  ar.sort()


#dfs
def dfs(n):

  for i in arr[n]:

    if visited[i] == False and i != V:
      visited[i] = True
      res_dfs.append(i)
      dfs(i)

res_dfs = [V]

dfs(V)

print(*res_dfs)



visited = [False for _ in range(N+1)]
res_bfs = []

#bfs
que = deque([V])
res_bfs = []
while len(que) != 0 :

  i = que.popleft()

  if visited[i] ==False:
    visited[i] = True
    res_bfs.append(i)

    for j in arr[i]:
      if visited[j] == False:

        que.append(j)

print(*res_bfs)