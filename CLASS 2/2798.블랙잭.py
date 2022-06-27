import itertools

N , M = map(int, input().split())

arr = list( map(int, input().split()))

tmp = list(itertools.combinations(arr,3))

res = 0
for i in range(len(tmp)) :

  comb = sum(tmp[i])

  if comb <= M:
    if res < comb:
      res = comb

print(res)