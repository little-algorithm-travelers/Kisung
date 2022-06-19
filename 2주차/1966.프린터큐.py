from collections import deque


T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  result = 0
  arr = deque(list(map(int, input().split())))

  while arr:
    
    lefttmp = arr.popleft()
    if len(arr) ==0:
      result +=1
      break
    
    M -= 1
    if M == -1:
      if lefttmp >= max(arr):
        result +=1
        break
      else:
        M = len(arr)
        arr.append(lefttmp)
    else:
      if lefttmp >= max(arr):
        result += 1
        
      else:
        arr.append(lefttmp)


  print(result)

