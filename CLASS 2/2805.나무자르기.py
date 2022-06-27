N, M = map(int, input().split())

arr = list(map(int, input().split()))


start = 0
end = max(arr)


while start <= end:
  mid = (start + end) // 2

  tmp = 0
  for i in arr:
    
    if i - mid > 0:
      tmp += i - mid

  if tmp >= M:

    start = mid +1


  else :
    end = mid -1

print(end)