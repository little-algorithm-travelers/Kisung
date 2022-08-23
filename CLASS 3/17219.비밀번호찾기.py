import sys


N, M = map(int,sys.stdin.readline().rstrip().split())

dic = dict()

for _ in range(N):

  www, pw = sys.stdin.readline().rstrip().split()

  dic[www] = pw

for _ in range(M):

  tmp = sys.stdin.readline().rstrip()
  print(dic[tmp])