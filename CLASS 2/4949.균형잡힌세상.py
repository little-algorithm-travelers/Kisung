while True:
  s = input()

  if s =='.':
    break

  stck = []

  chck = False

  for i in s:

    if i == '(':
      stck.append(i)
    elif i == '[':
      stck.append(i)
    


    elif i == ')':
      if len(stck) == 0:
        chck = True
        break
      tmp = stck.pop()

      if '(' != tmp:
        chck = True
        break
    elif i == ']':
      if len(stck) == 0:
        chck = True
        break
      tmp = stck.pop()

      if '[' != tmp:
        chck = True
        break

  if chck ==True or len(stck) != 0:
    print('no')
  else:
    print('yes')
