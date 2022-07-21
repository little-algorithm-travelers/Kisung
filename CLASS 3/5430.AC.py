from collections import deque



T = int(input())

for _ in range(T):

  #명령어
  p = input()

  #배열 수
  n = int(input())

  x = input()
  #배열
  if n != 0:
    q = deque(list(map(int,x[1:-1].split(","))))
  else:
    q = deque()
  R = False
  err = False
  for i in p:

    if i == "R":
      if R == False:
        R = True
      else:
        R = False

    
    else:
      if len(q) == 0:
        err = True
        break
      if R == False:
        q.popleft()
      else:
        q.pop()

  if R == True:
    q.reverse()
  
  if err == True:
    print("error")
  else:
    print("[",end="")
    print(*q,sep=",",end="")
    print("]")