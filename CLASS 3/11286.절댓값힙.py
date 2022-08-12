import heapq
import sys
Q = []

N = int(sys.stdin.readline().rstrip())

for _ in range(N):

  n = int(sys.stdin.readline().rstrip())

  if n == 0:

    if len(Q) == 0:
      print(0)
    else:

      tmp = heapq.heappop(Q)
      print(tmp[1])
  else:
    heapq.heappush(Q,[abs(n),n])
