

from collections import deque


N = int(input())

arr = deque([i for i in range(1,N+1)])

tmp = True


while len(arr) > 1:

  if tmp == True:
    arr.popleft()
    tmp =False
  else:
    tmp = True
    num = arr.popleft()
    arr.append(num)

print(arr[0])


