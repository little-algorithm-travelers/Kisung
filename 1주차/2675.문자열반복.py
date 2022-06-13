T = int(input())

for i in range(T):
  N, string= input().split()
  N = int(N)

  tmp =""
  for j in string:
    tmp += j*N
  print(tmp)