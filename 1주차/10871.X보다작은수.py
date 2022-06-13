N, X = map(int,input().split())
arr = list(map(int, input().split()))
tmp = ""
for i in arr:
  if i < X:
    tmp += str(i)
    tmp +=" "
print(tmp)