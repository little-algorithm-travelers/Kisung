T = int(input())

arr = [1,2,3]

dp = [0,1,2,4,0,0,0,0,0,0,0]


for i in range(4,11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for _ in range(T):

  n = int(input())

  print(dp[n])


# https://www.acmicpc.net/board/view/95422
# A(n)은,

# - A(n-1), 즉 n-1을 만드는 모든 경우 각각에 대해 그 뒤에 1을 더하는 것과

# - A(n-2), 즉 n-2를 만드는 모든 경우 각각에 대해 그 뒤에 2를 더하는 것과

# - A(n-3), 즉 n-3을 만드는 모든 경우 각각에 대해 그 뒤에 3을 더하는 것

# 의 모든 경우의 수의 합이기 때문입니다.