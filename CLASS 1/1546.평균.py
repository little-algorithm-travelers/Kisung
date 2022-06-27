N = input()
scores = list(map(int, input().split()))

top = max(scores)



for i in range(len(scores)):
  
  scores[i] = scores[i]/top*100

print(sum(scores)/len(scores))