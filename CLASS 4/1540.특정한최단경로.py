import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):

  s, e, t =  map(int, input().split())

  graph[s].append([e,t])
  graph[e].append([s,t])


u, v = map(int, input().split())

INF = int(1e7)


def dijkstra(start):

  distance = [INF for _ in range(N + 1)]
  distance[start] = 0
  Q = []

  heapq.heappush(Q,[0,start])

  while Q:

    dist , now = heapq.heappop(Q)

    if distance[now] < dist:
      continue

    for  nextnode, nextcost in graph[now]:
      
      total = nextcost + dist

      if distance[nextnode] > total:

        distance[nextnode] = total
        heapq.heappush(Q,[total, nextnode])

  return distance




first = dijkstra(1)

udijk = dijkstra(u)

vdijk = dijkstra(v)

uv = udijk[v]

m = min(first[u] + vdijk[N] + uv, first[v] + udijk[N] + uv)

if m >= INF:
  print(-1)
else:
  print(m)




