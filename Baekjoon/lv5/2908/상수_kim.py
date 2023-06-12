#str = ['734','893']
str = input().split()
#문자열 슬라이싱을 이용해 뒤집기 
N = str[0][::-1]
M = str[1][::-1]
if int(N) > int(M):
    print(N)
else:
    print(M)