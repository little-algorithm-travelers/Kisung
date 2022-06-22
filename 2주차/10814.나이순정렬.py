N = int(input())

arr = []

for _ in range(N):

  age, name = input().split()

  age = int(age)

  tmp = [age,name]
  arr.append(tmp)
arr.sort(key= lambda x : x[0])

for i in arr:
  print(*i)