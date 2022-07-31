from collections import deque

M, N, H =  map(int,input().split())

arr = []


for _ in range(H):
  tmp = []
  for _ in range(N):

    tmp1 = list(map(int,input().split()))

    tmp.append(tmp1)
  arr.append(tmp)


dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,1,-1]

q = deque()

for k in range(H):
  for i in range(N):
    for j in range(M):

      if arr[k][i][j] == 1:
        q.append([k,i,j])


while q:

  t = q.popleft()

  x = t[2]
  y = t[1]
  z = t[0]

  for a in range(6):

    nx = x + dx[a]
    ny = y + dy[a]
    nz = z + dz[a]

    if nx >= 0 and ny >= 0 and nz >= 0 and nx < M and ny < N and nz < H:

      if arr[nz][ny][nx] == 0:
        arr[nz][ny][nx] = arr[z][y][x] + 1
        q.append([nz,ny,nx])

res_max = 0
zero  = False
for k in range(H):
  for i in range(N):
    for j in range(M):

      if arr[k][i][j] > res_max:
        res_max = arr[k][i][j]
      if arr[k][i][j] == 0:
        zero = True
    
    if zero == True:
      break

  if zero == True:
    break

if zero :
  print(-1)
else:
  print(res_max-1)




