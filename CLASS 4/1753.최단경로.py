import sys

import heapq

input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
  
  u,v,w = map(int,input().split())

  graph[u].append([v,w])

Q = []

INF = int(1e9)
res = [INF] * (V+1)

res[K] = 0


heapq.heappush(Q,[0,K])

while Q:
  #현재 노드
  weight, node = heapq.heappop(Q)

  if res[node] < weight:
    continue

  #이동할 다음 노드 체크
  for new, w in graph[node]:

    total = weight + w

    if res[new] > total:

      res[new] = total
      heapq.heappush(Q,[res[new], new])

for i in range(1,V+1):
  if res[i] == INF:
    print('INF')
  else:
    print(res[i])