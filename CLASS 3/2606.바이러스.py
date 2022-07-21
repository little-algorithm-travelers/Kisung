from queue import Queue


N = int(input())

M = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(M):

  a, b = map(int, input().split())

  arr[a].append(b)
  arr[b].append(a)

res = [0 for _ in range(N+1)]


que = Queue()

que.put(1)

while not que.empty():

  tmp = que.get()
  if res[tmp] == 1:
    continue

  res[tmp] +=1

  for i in arr[tmp]:

    que.put(i)


print(sum(res)-1)