H, W = map(int, input().split())

chess = list()

for i in range(H):
  tmp = input()
  chess.append(tmp)



result =99999
for i in range(H-8+1):
  for j in range(W-8+1):
    W_start =0
    B_start =0
    for k in range(i, i+8):
      for l in range(j,j+8):

        #짝수칸
        if (k + l) %2 == 0:
          if chess[k][l] =='W':
            B_start +=1
          else:
            W_start +=1
        #홀수칸
        else:
          if chess[k][l] == 'B':
            B_start +=1
          else:
            W_start +=1
    result = min(W_start,B_start,result)

print(result)
