T = int(input())

for _ in range(T):

  H,W,N = map(int, input().split())

  
  X = N % H
  

  Y = N // H +1

  if X == 0:
    X = H
    Y -=1 

  if Y < 10:
    print(str(X)+'0'+str(Y))
  else:
    print(str(X)+str(Y))