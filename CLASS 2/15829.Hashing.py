L = int(input())

s = input()

r = 31
M = 1234567891


res =0

for i in range(L):
  res += (ord(s[i])- 96) * (r**i)
  res %= 1234567891

print(res)
