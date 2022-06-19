N = int(input())

arr = list(map(int, input().split()))
cnt = 0
for i in arr:
  if i == 1:
    continue

  sosu = True
  for j in range(2,i-1):
    if i % j == 0:
      sosu = False
      break
  
  if sosu:
    cnt +=1

print(cnt)