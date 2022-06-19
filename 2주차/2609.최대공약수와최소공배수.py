
import math



N, M = map(int, input().split())
def lcm(a,b):
  return (a * b) // math.gcd(a,b)
print(math.gcd(N,M))
print(lcm(N,M))