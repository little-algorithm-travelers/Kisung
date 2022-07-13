N, M = map(int, input().split())


pan = [[999999 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):

  a, b = map(int, input().split())

  pan[a][b] = 1
  pan[b][a] = 1


for i in range(1,N+1):


  for j in range(1,N+1):
    pan[j][j] = 0
    for k in range(1, N+1):

      pan[j][k] = min(pan[j][k], pan[j][i] + pan[i][k])

res = 999999
res_cnt = 999999

for i in range(1, N+1):

  tmp =0
  for j in range(1,N+1):

    tmp += pan[i][j]

  if res > tmp:
    res = tmp
    res_cnt = i

print(res_cnt)
