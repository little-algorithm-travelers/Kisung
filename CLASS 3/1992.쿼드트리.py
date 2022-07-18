N = int(input())

arr = []

for _ in range(N):
  tmp = input()
  arr.append(tmp)

res = ""


def tree(x,y,size):

  global res

  base = arr[x][y]
  check = False

  for i in range(x, x+size):
    for j in range(y,y+size):
      if arr[i][j] != base:
        check = True
        break
  if check == False:
    res +=base
  else:
    res +="("

    tree(x,y,size//2)
    tree(x  ,y+ size//2,size//2)
    tree(x+ size//2,y ,size//2)
    tree(x + size//2,y + size//2,size//2)
    res += ")"

tree(0,0,N)
print(res)
  