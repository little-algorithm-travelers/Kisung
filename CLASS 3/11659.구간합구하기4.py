import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))


for i in range(1,len(arr)):

  arr[i] += arr[i-1]






for _ in range(M):

  i,j = map(int, sys.stdin.readline().split())
  i -=1
  j -=1
  if i == 0:
    print(arr[j])
  else:
    print(arr[j] - arr[i-1])