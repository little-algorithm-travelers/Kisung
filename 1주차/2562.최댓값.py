num = 0
idx = 0
for i in range(9):
  tmp = int(input())
  if num < tmp:
    num = tmp
    idx = i
print(num)
print(idx+1)