# import sys
# sys.setrecursionlimit(10**8)

# N, r, c = map(int, input().split())

# cnt = 0

# def zsearch(x,y, l):
#   global cnt
#   global r,c
#   l //= 2

#   if l ==1:
#     if x == r and y == c:

#       print(cnt)

#     elif x == r and y+1 == c:
#       print(cnt+1)

#     elif x+1 == r and y == c:
#       print(cnt+2)

#     elif x+1 == r and y+1 == c:
#       print(cnt+3)

#   #1사분면 검색
#   if c < x +l and r < y + l:
#     zsearch(x , y , l)

#   #2사분면 검색
#   elif c >= x + l and r < y + l:
#     cnt += l*l
#     zsearch(x , y + l , l)

#   #3사분면 검색
#   elif c < x +l and r >= y + l:
#     cnt += l*l*2
#     zsearch(x + l, y , l)

#   #4사분면 검색
#   elif c >= x +l and r >= y + l:

#     cnt += l*l*3
#     zsearch(x + l, y + l, l)

# le = 2**N

# zsearch(0,0,le)


#######https://ggasoon2.tistory.com/11

N, r, c = map(int, input().split())

ans = 0

while N != 0:

	N -= 1

	# 1사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 2사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)
