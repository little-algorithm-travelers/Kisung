T = int(input())

arr = [0 for _ in range(101)]

arr[0] = 1
arr[1] = 1
arr[2] = 1

for i in range(3,101):

  arr[i] = arr[i-2] + arr[i-3]



for _ in range(T):
  idx = int(input())-1
  print(arr[idx])