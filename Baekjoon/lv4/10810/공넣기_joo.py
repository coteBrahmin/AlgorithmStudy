import sys
N, M = map(int, sys.stdin.readline().split())

#N개의 바구니를 딕셔너리 형태로 만듭니다.
dict = {i: 0 for i in range(1,N+1)}

#num1~num2까지 바구니에 new 번호가 적힌 공을 넣게 됩니다. 인풋값을 for문을 통해 받아옵니다.
#그러니 for문을 한번 더 써서 dict의 값을 재할당합니다.
# 재할당된 값을 출력합니다.
for i in range(1, M+1):
    num1, num2, new = map(int, sys.stdin.readline().split())
    for j in range(num1, num2+1):
        dict[j] = new
print(*dict.values())