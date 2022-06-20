T = int(input())

apart = []

arr = [i for i in range(1,15)]

apart.append(arr)

for i in range(14):

  sum1 =0
  tmp = []
  for j in range(14):

    sum1 += apart[i][j]
    tmp.append(sum1)

  apart.append(tmp)




for _ in range(T):
  k = int(input())
  n = int(input())

  print(apart[k][n-1])
  