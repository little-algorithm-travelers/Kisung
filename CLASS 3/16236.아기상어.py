# https://hooongs.tistory.com/291
# https://codingmovie.tistory.com/40

from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline().rstrip())

arr = []

shark_x, shark_y = 0,0
shark_size = 2

for i in range(N):

  tmp = list(map(int,sys.stdin.readline().rstrip().split()))
  if 9 in tmp:
    shark_x = i
    shark_y = tmp.index(9)
  arr.append(tmp)

arr[shark_x][shark_y] = 0

def findfish(x,y):

  Q = deque()

  Q.append([x,y,0])

  visited = [[False ]* N for _ in range(N) ]

  fishes = []
  while Q:

    qx,qy,cnt = Q.popleft()

    visited[qx][qy] = True

    if 0 < arr[qx][qy] < shark_size:
      fishes.append([qx,qy,cnt])


    for i in range(4):

      nx, ny = qx+dx[i], qy+dy[i]

      if -1 < nx < N and -1 < ny < N:
        if not visited[nx][ny]:
          if arr[nx][ny] <= shark_size:
            visited[nx][ny] = True
            Q.append([nx,ny,cnt+1])

  if fishes:

    fishes.sort(key= lambda x : (x[2], x[0], x[1]) )

    return fishes[0]
  else:
    return -1

res = 0
eatcnt = 0
while True:

  fish = findfish(shark_x,shark_y)

  if fish == -1 :
    break
  else:
    x,y,time = fish

  eatcnt +=1
  if eatcnt == shark_size:
    eatcnt =0
    shark_size += 1

  shark_x = x
  shark_y = y
  arr[x][y] = 0
  res += time

print(res)