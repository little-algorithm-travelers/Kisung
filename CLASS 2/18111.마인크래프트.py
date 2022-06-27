import sys


N, M, B = map(int,input().split())

mapp = []

avg = 0

for _ in range(N):
  tmp1 = sys.stdin.readline().strip()

  tmp = list(map(int,tmp1.split()))
  avg += sum(tmp)
  mapp.append(tmp)


res_time = 99999999
res_height = 0

for i in range(257):

  plus = 0
  minus = 0
  for j in range(N):
    for k in range(M):

      if mapp[j][k] > i:
        minus += mapp[j][k] - i
      else:
        plus += i - mapp[j][k]
  
  if B + minus < plus:

    continue
  
  if res_time >= minus*2+plus:
    res_time = minus*2+plus
    res_height = i

print(res_time, res_height)

