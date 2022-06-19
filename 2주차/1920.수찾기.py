N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
arr = list(map(int, input().split()))

for i in arr:
  start =0
  end = N -1

  while start <= end:
    
    mid = (start + end) // 2

    if A[mid] < i :
      start = mid + 1
    elif A[mid] > i :
      end = mid -1

    else:
      end = mid
      break

  if A[end] == i:
    print(1)
  else:
    print(0)