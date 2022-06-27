while True:
  num = input()
  if num == '0':
    break
  yn = True
  for i in range(len(num)//2):

    if num[i] != num[-i-1]:
      yn = False
      break
  
  if yn == True:
    print('yes')
  else:
    print('no')