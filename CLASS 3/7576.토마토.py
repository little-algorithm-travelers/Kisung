from collections import deque

M, N =  map(int,input().split())

arr = []


for _ in range(N):


  tmp = list(map(int,input().split()))

  arr.append(tmp)


dx = [0,0,-1,1]
dy = [-1,1,0,0]


q = deque()


for i in range(N):
  for j in range(M):

    if arr[i][j] == 1:
      q.append([i,j])


while q:

  t = q.popleft()

  x = t[1]
  y = t[0]


  for a in range(4):

    nx = x + dx[a]
    ny = y + dy[a]


    if nx >= 0 and ny >= 0  and nx < M and ny < N :

      if arr[ny][nx] == 0:
        arr[ny][nx] = arr[y][x] + 1
        q.append([ny,nx])

res_max = 0
zero  = False

for i in range(N):
  for j in range(M):

    if arr[i][j] > res_max:
      res_max = arr[i][j]
    if arr[i][j] == 0:
      zero = True
  
  if zero == True:
    break


if zero :
  print(-1)
else:
  print(res_max-1)




