N = int(input())


for i in range(N):

  S = str(i)
  sum1 = i
  for j in S:
    sum1 += int(j)
  
  if sum1 == N:
    print(i)
    break
  
  if i == N-1:
    print(0)
