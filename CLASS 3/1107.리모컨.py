
N = int(input())

M = int(input())

if M !=0:
  arr = list(map(int,input().split()))
else:
  arr = []

## 작거나 100과 가까운수 처리
cur =100

pm = abs(N-cur)

if 97 <= N <= 103:
  print(abs(100 - N))



elif len(str(N)) <3:
  res = 100
  for i in range(0,96):
    next_num =False

    for j in arr:

      if str(j) in str(i):
        next_num = True
        break
        
    #고장난 키 있으면 넘어가기
    if next_num == True:
      continue

    #몇번 눌러라야하는지 계산
    if res > abs(N - i)+ len(str(i)):
      res = abs(N - i) + len(str(i))

  print(min(pm,res) )

#################큰수 처리가지 방법

else:
#범위
  size = N
  #결과
  res = 500000

  for i in range(N-size,N+size):

    next_num =False

    for j in arr:

      if str(j) in str(i):
        next_num = True
        break
        
    #고장난 키 있으면 넘어가기
    if next_num == True:
      continue

    #몇번 눌러라야하는지 계산
    if res > abs(N - i) + len(str(i)):
      res = abs(N - i) + len(str(i))


  print(min(pm,res) )

