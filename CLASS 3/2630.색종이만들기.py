N = int(input())

arr = []

for _ in range(N):

  tmp = list(map(int, input().split()))

  arr.append(tmp)


white = 0
blue = 0

def cut(x,y,size):

  global white,blue

  base = arr[x][y]
  check = False

  for i in range(x, x+size):

    for j in range(y, y+size):

      if arr[i][j] != base:
        check = True

  if check == False:
    if base == 0:
      white +=1
    else:
      blue +=1
  else:

    cut(x, y, size//2)
    cut(x + size//2, y, size//2)
    cut(x, y + size//2, size//2)
    cut(x + size//2, y + size//2, size//2)

cut(0,0,N)
print(white,blue,sep="\n")