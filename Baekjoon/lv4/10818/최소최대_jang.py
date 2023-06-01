n = int(input())
num = list(map(int, input().split()))

print(min(num), max(num))

# 리스트에 max(), min()함수 사용하여 최대값, 최소값 도출
# 이를 사용하기 위해 입력값 받을 때 리스트로 형변환