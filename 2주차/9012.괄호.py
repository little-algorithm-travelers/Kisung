T = int(input())

for _ in range(T):

  s = input()

  stck = []

  chk = False
  for i in s:

    if i == '(':
      stck.append(i)

    else:

      if len(stck) == 0:
        
        chk =True
        break

      tmp = stck.pop()

  if len(stck) != 0:
    chk = True

  if chk == True:
    print('NO')
  else:
    print('YES')