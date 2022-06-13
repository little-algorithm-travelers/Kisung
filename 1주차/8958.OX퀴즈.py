T = int(input())

for _ in range(T):
  s = input()

  score = 0
  cnt = 0
  for i in s:
    if i == 'O':
      cnt += 1
      score += cnt
    else:
      cnt =0
  print(score)
    