import itertools


N, K = map(int, input().split())


arr = [0 for _ in range(N)]

print(len(list(itertools.combinations(arr,K))))