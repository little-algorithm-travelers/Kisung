N = int(input())

arr = []
res = [1 for _ in range(N)]

for _ in range(N):
  tmp = list(map(int, input().split()))

  arr.append(tmp)


for i in arr:

  for j in range(N):

    if i[0] ==arr[j][0] and i[1] == arr[j][1]:
      continue

    elif i[0] > arr[j][0] and i[1] > arr[j][1]:
      res[j] +=1

print(*res)