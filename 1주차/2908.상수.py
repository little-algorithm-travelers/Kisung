A,B = input().split()

A1 =""
for i in A:
  A1 = i+A1

B1 =""
for i in B:
  B1 = i+B1

int(A1)
int(B1)

print(max(A1,B1))