import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

answer = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)
#https://donghak-dev.tistory.com/27

# N = int(input())

# M = int(input())

# S = input()

# ioi = "I"+ "OI"*N

# res = 0

# for i in range(0,M-len(ioi)):

#   eq = True
#   for j in range(i, i+len(ioi)):

#     if S[j] != ioi[j-i]:
#       eq = False
#       break
  
#   if eq == True:
#     res +=1
#   else:
#     continue

# print(res)


