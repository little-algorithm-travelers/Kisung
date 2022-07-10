minus_split = input().split("-")

if len(minus_split) ==1:

  plus_split = list(map(int, minus_split[0].split("+")))

  print(sum(plus_split))

else:
  res = 0
  for i in range(len(minus_split)):

    if i == 0:
      plus_split = list(map(int, minus_split[i].split("+")))
      res +=(sum(plus_split))
    else:
      plus_split = list(map(int, minus_split[i].split("+")))
      res -=(sum(plus_split))
  print(res)