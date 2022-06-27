
import collections

str = input().upper()
counter = collections.Counter(str)

most2 = counter.most_common(n=2)

if len(most2) == 1 :
  print(most2[0][0])
else:

  if most2[0][1] == most2[1][1]:
    print("?")
  else:
    print(most2[0][0])
