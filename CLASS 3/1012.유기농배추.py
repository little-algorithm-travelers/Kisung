import sys

sys.setrecursionlimit(10**6)
def dfs(x,y):

  visited[x][y] = True

  for i in range(4):

    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and ny >= 0 and nx < N and ny < M:

      if visited[nx][ny] == False and mapp[nx][ny] == 1:
        dfs(nx,ny)




T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
  M, N, K = map(int, input().split())

  mapp = [[0 for _ in range(M)] for _ in range(N)]

  visited = [[False for _ in range(M)] for _ in range(N)]

  for _ in range(K):
    
    X,Y = map(int,input().split())
    mapp[Y][X] +=1

  cnt = 0

  for i in range(N):
    for j in range(M):


      if mapp[i][j] == 1 and visited[i][j] == False:
        cnt += 1
        dfs(i,j)




  print(cnt)










