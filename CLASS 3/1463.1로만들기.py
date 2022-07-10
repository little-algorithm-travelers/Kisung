N = int(input())

arr = [0 for _ in range(N+1)]

for i in range(2,N+1):

  arr[i] = arr[i-1]+1
  if i%3 == 0:
    arr[i] = min(arr[i//3]+1, arr[i])
  if i%2 ==0:
    arr[i] = min(arr[i//2]+1, arr[i])


print(arr[N])
