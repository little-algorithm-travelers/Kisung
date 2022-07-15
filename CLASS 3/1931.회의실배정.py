N = int(input())

arr =[]

for _ in range(N):
  tmp = list(map(int, input().split()))

  arr.append(tmp)
arr.sort()
arr.sort(key=lambda x: x[1])


cnt = 0

end = 0

for i in arr:

  if i[0] >=end:
    cnt +=1
    end = i[1]


print(cnt)



