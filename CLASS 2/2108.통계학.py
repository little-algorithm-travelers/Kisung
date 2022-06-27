import collections

N = int(input())

arr = []
for _ in range(N):
  a = int(input())
  arr.append(a)
arr.sort()


print(round((sum(arr)/N)))
print(arr[len(arr)//2])

cnt = collections.Counter(arr).most_common(2)

if len(arr) >1:
  if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
  else:
    print(cnt[0][0])
else:
  print(cnt[0][0])





print(max(arr)-min(arr))

