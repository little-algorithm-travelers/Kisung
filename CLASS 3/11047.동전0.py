N, K = map(int, input().split())

arr = []

for _ in range(N):

  arr.append(int(input()))

coin = 0

for i in reversed(arr):

  if i > K:
    continue

  coin += K //i
  K -= (K//i) * i

  if K == 0:
    break
print(coin)