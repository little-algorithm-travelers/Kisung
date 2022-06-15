N = int(input())
num = 0
cnt = 0
while True:
  num +=1

  strnum = str(num)
  if "666" in strnum:
    cnt +=1
    if cnt == N:
      break

print(num)
  