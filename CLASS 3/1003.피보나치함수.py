T = int(input())

fib = [[1,0],[0,1]]





for i in range(2,41):

  a = fib[i-2][0] + fib[i-1][0]
  b = fib[i-2][1] + fib[i-1][1]


  fib.append([a,b])




for _ in range(T):
  
  N = int(input())

  print(fib[N][0],fib[N][1])