
N = int(input())

if N == 1:
  print(1)
  
else:
  N -=1
  cnt = 1
  for i in range(6,N*N*100,6):

    

    N -= i
    cnt+=1
    if N <= 0:
      break
    
  print(cnt)
