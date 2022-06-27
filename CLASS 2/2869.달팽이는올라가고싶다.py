A,B,V = map(int, input().split())

day =0
diff = A -B
if A == V:
  print(1)

else:

  day += 1

  V -= A

  if V <= 0:
    print(day)

  else:

    

    if V % diff == 0:
      day += V//diff
    else:
      day += V//diff +1
    print(day)

