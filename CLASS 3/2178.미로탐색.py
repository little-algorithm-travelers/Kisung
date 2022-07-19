from collections import deque

N, M = map(int, input().split())

arr = []

for _ in range(N):

  tmp = input()
  t = []
  for i in tmp:
    t.append(int(i))
  arr.append(t)

cnt =1



def bfs(x,y):
  global cnt
  que = deque()
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  que.append([x,y])
  a = True
  while a:

    tmp = que.popleft()


    for i in range(4):

      nx = tmp[0] + dx[i]
      ny = tmp[1] + dy[i]


      if nx >=0 and ny >= 0 and nx < N and ny < M:

        if arr[nx][ny] == 1:
          que.append([nx,ny])
          arr[nx][ny] += arr[tmp[0]][tmp[1]]

        if nx == N-1 and ny ==M-1:
          a = False


bfs(0,0)

print(arr[N-1][M-1])

      