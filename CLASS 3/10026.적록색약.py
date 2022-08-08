import sys
sys.setrecursionlimit(100000)
def dfs(x,y,color):

  for dx, dy in [(1,0), (-1,0), (0,1),(0,-1)]:

    nx = x + dx
    ny = y + dy
    
    if 0 <= nx < N and 0 <= ny < N:

      if arr[nx][ny] == color and V[nx][ny] == False:

        V[nx][ny] = True
        dfs(nx, ny, color)

def dfs2(x,y,color):

  for dx, dy in [(1,0), (-1,0), (0,1),(0,-1)]:

    nx = x + dx
    ny = y + dy
    
    if 0 <= nx < N and 0 <= ny < N:

      if arr2[nx][ny] == color and V[nx][ny] == False:

        V[nx][ny] = True
        dfs2(nx, ny, color)

N = int(input())

arr = []


res1 = 0
res2 = 0

for _ in range(N):

  tmp = list(input())
  arr.append(tmp)


V = [[False for _ in range(N)] for _ in range(N)]


for r in range(N):

  for c in range(N):

    if V[r][c] == False:
      V[r][c] = True
      res1 += 1
      dfs(r,c,arr[r][c])

######################
arr2 = []

for i in range(N):
  tmp = []
  for j in range(N):

    if arr[i][j] == 'R' or arr[i][j] == 'G':
      tmp.append('R')
    else:
      tmp.append('B')
  arr2.append(tmp)

V = [[False for _ in range(N)] for _ in range(N)]

for r in range(N):

  for c in range(N):

    if V[r][c] == False:
      V[r][c] = True
      res2 += 1
      dfs2(r,c,arr2[r][c])


print(res1,res2)