import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

sarr = sorted(arr)

rank = dict()

r = 0
before = 0
for now in sarr:

  if now == before:
    continue
  rank[now] = r
  before = now
  r += 1


for i in arr:

  print(rank[i],end=' ')