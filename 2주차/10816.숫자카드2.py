from collections import Counter


N = int(input())

narr = list(map(int, input().split()))

M = int(input())

marr = list(map(int, input().split()))


cnt = Counter(narr)

for i in marr:

  print(cnt[i], end=' ')