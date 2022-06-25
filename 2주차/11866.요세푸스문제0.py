from collections import deque


N, K = map(int, input().split())

arr = deque(i for i in range(1,N+1))
res = []

cnt = 0

tmp = 0
while len(arr) > 0:
  cnt+=1
  if cnt % K == 0:
    tmp = arr.popleft()
    res.append(tmp)
  else:
    tmp = arr.popleft()
    arr.append(tmp)


str1 ='<'
for i in range(N):

  str1 += str(res[i])

  if i != N-1:
    str1 += ', '

str1 +='>'

print(str1)