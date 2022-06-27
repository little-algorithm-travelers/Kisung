words = set()

N = int(input())

for i in range(N):
  words.add(input())

words = list(words)
words.sort()
words.sort(key=len)

for i in words:
  print(i)