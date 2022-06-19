M,N = map(int, input().split())

arr = [True for _ in range(N+1)]

result = []
for i in range(2, N+1):

  if arr[i] == True:
    result.append(i)
  for j in range(i, N+1, i):
    arr[j] = False


for i in result:
  if M <= i <= N :
    print(i)


