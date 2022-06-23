import sys


N = int(input())

arr =[0 for _ in range(10001)]
for _ in range(N):
  tmp = int(sys.stdin.readline().strip())

  arr[tmp] +=1



for i in range(10001):
  if arr[i]==0:
    continue

  for _ in range(arr[i]):
    print(i)