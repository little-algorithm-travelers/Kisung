import collections
from typing import Counter;

N, M = map(int,input().split())


arr =[]
for _ in range(N+M):
  tmp = input()
  arr.append(tmp)

cnt = Counter(arr)

res = []
for i in cnt:
  if cnt[i] == 2:
    res.append(i)

res.sort()
print(len(res))
print(*res,sep="\n")