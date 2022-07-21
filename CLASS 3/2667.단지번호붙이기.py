N = int(input())

arr = []

for _ in range(N):

  tmp = list(map(int, input()))

  arr.append(tmp)



dx = [0,0,-1,1]
dy = [-1,1,0,0]

cnt = 0 
def dfs(x,y):
  global cnt

  if arr[x][y] ==1:

    cnt+=1
    arr[x][y] = 0
  
  for i in range(4):

    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and ny >= 0 and nx < N and ny < N:
      if arr[nx][ny] == 1:
        dfs(nx,ny)

res = []

for i in range(N):
  for j in range(N):

    if arr[i][j] == 0:
      continue

    dfs(i,j)
    res.append(cnt)
    cnt =0

print(len(res))
res.sort()
print(*res,sep="\n")

