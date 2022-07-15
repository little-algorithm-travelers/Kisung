from queue import PriorityQueue
import sys

N = int(sys.stdin.readline().strip())

que = PriorityQueue()

for _ in range(N):

  tmp = int(sys.stdin.readline().strip())

  if tmp == 0:

    if not que.empty():
      print(que.get())
    else:
      print(0)
  
  else:
    que.put(tmp)


