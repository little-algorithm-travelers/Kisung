import sys

M = int(sys.stdin.readline().rstrip())

S = []

for _ in range(M):

  tmp = sys.stdin.readline().rstrip()

  if tmp == 'all':
    S = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    continue
  elif tmp == 'empty':
    S = []
    continue
  
  else:
    tmp1, tmp2 = tmp.split()

  if tmp1 == 'add':
    if tmp2 not in S:
      S.append(tmp2)
  
  elif tmp1 == 'remove':
    if tmp2 in S:
      S.remove(tmp2)

  elif tmp1 == 'check':
    if tmp2 in S:
      print(1)
    else:
      print(0)
  elif tmp1 == 'toggle':
    if tmp2 in S:
      S.remove(tmp2)
    else: 
      S.append(tmp2)



  
