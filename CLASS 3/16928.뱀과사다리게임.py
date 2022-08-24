from collections import deque
import sys

N,M  = map(int, sys.stdin.readline().rstrip().split())

move = dict()


for _ in range(N + M ):
  start, end = map(int, sys.stdin.readline().rstrip().split())

  move[start] = end




pan = [0 for _ in range(101)]

Q = deque()

Q.append([1,0])

while True:

  now, val = Q.popleft()
  if pan[now] != 0:
    continue
  if now == 100:
    print(val)
    break

  pan[now] = val


  for i in range(1,7):

    newnow = now + i
    if newnow > 100:
      continue

    if newnow in move.keys():
      Q.append([move[newnow],val+1])
      
    else:
      Q.append([newnow,val+1])
