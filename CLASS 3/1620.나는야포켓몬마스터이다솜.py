import sys

N, M = map(int,input().split())

arr = ["0"]
dic = dict()
for i in range(N):
  tmp = sys.stdin.readline().strip()

  arr.append(tmp)

  dic[tmp] = i+1

for _ in range(M):

  tmp = input()


  if tmp.isalpha():
    print(dic[tmp])
  else :
    print(arr[int(tmp)])


