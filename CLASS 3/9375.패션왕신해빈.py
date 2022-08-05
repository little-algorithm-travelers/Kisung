T = int(input())

for _ in range(T):

  n = int(input())

  dic = dict()

  closet = []

  idx = 0
  for i in range(n):

    item, cate = input().split()

    if cate not in dic.keys():
      dic[cate] = idx
      tmp = [item]
      closet.append(tmp)
      idx += 1
    else:

      closet[dic[cate]].append(item)

  res = 1
  for i in closet:

    res *= len(i)+1

  print(res-1)