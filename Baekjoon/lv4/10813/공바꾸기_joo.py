import sys

N, M = map(int, sys.stdin.readline().split())
#바구니(key)와 같은 번호의 공(value)을 갖고 있으니 딕셔너리 형태로 만들어 주었습니다. 
dict = {i: i for i in range(1, N + 1)} 

#swap 코드를 구글링하여 이용하였습니다. 
for i in range(1, M + 1):
    x, y = map(int, sys.stdin.readline().split())
    dict[x], dict[y] = dict[y], dict[x]

print(*dict.values())