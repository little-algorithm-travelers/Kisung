# https://bbbyung2.tistory.com/62

import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):

  s, e, t = map(int, input().split())

  graph[s].append([e,t])

INF = int(1e9)

def dijkstra(start):

  Q = []

  distance = [INF for _ in range(N + 1)]

  distance[start] = 0
  heapq.heappush(Q, [0,start])

  while Q:
    #dist : 지금까지 걸린 시간(거리)
    #now : 현재 노드 번호
    dist, now  = heapq.heappop(Q)

    if distance[now] < dist:
      continue

    #다음 연결된 노드 탐방하는 반복문
    for index, cost in graph[now]:
      # 다음 노드까지의 시간(거리) 계산
      total = dist + cost
      #갱신할 가치가 있다면
      if distance[index] > total:
        #최단거리라 보고 갱신
        distance[index] = total
        #최단거리라고보고 힙큐에 넣기
        heapq.heappush(Q, [total, index])
  
  return distance


back = dijkstra(X)
result = 0
for i in range(1, N + 1):
    go = dijkstra(i)

    result = max(result, go[X] + back[i])


print(result)