N = int(input())

arr = []

for _ in range(N):

  xy = list(map(int,input().split()))

  arr.append(xy)


arr.sort(key=lambda x : x[0])

arr.sort(key=lambda x : x[1])

for i in arr:
  print(i[0],i[1])