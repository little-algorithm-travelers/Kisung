from queue import PriorityQueue
import sys

N = int(sys.stdin.readline().rstrip())

Q = PriorityQueue()

for _ in range(N):

  cmd = sys.stdin.readline().rstrip()
  
  if cmd == '0':

    if Q.empty():
      print(0)
    else:
      print(Q.get() * -1)
  
  else:
    Q.put(int(cmd) * -1)

