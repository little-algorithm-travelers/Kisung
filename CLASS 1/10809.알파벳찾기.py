S = input()

arr = [ -1 for _ in range(26)]
for i in range(len(S)):
  if arr[ord(S[i]) -97] == -1:
    arr[ord(S[i]) -97] = i

tmp = ""

for i in range(26):
  tmp += str(arr[i])
  if i !=25:
    tmp +=" "
print(tmp)