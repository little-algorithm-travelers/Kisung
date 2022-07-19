
N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2] 

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])  

    print(dp[N])

#https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802579%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-DP