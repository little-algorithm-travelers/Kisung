N = int(input())

arr = []

for _ in range(N):
  tmp = list(map(int, input().split()))

  arr.append(tmp)

minus =0
zero = 0
plus = 0

def paper(x,y,size):

  global minus, zero, plus
  
  check = arr[x][y]

  for i in range(x, x+size):
    for j in range(y, y+size):

      if arr[i][j] !=check:
        for k in range(3):
          for l in range(3):

            paper(x + k * size//3, y + l * size//3 , size // 3)
        return
  
  if check ==-1:
    minus +=1
  
  elif check ==0:
    zero +=1
  else :
    plus +=1

paper(0,0,N)

print(minus)
print(zero)
print(plus)

#https://zidarn87.tistory.com/385