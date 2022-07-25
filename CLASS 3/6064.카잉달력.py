def num(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))
#https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-6064%EB%B2%88-%EC%B9%B4%EC%9E%89%EB%8B%AC%EB%A0%A5-Python-%EB%B8%8C%EB%A3%A8%ED%8A%B8-%ED%8F%AC%EC%8A%A4

# T = int(input())

# for _ in range(T):

#   M,N,x,y = map(int, input().split())

#   i,j = 0,0

#   check = False
#   for k in range(M*N):
#     i +=1

#     j +=1

#     if i >M:
#       i = 1
#     if j > N:
#       j = 1

#     if i == x and j == y:
#       check = True
#       print(k+1)
#       break


    


  
#   if check == False:
#     print(-1)