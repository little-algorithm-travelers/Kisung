arr = [0 for _ in range(43)]
num = 0
for i in range(10):
  a = int(input())
  a %= 42
  if arr[a] == 0:
    num +=1
    arr[a] +=1
print(num)
