import sys

Input = sys.stdin.readline

N = int(Input().rstrip())

arr = []
for _ in range(N):

  arr.append(list( map( int,   Input().rstrip().split())))


for i in range(1,N):

  arr[i][0] += min(arr[i-1][1],arr[i-1][2])
  arr[i][1] += min(arr[i-1][0],arr[i-1][2])
  arr[i][2] += min(arr[i-1][0],arr[i-1][1])


arr[-1].sort()

print(arr[-1][0])
