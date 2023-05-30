# 나중에 리스트 메소드를 사용하여 최대값을 간단하게 도출하기 위해 입력값을 받아 리스트로 형변환
dice = list(map(int, input().split()))

# 1. 세 값이 모두 같은 경우
if dice[0] == dice[1] and dice[1] == dice[2]:
    p = 10000 + dice[0] * 1000
# 2. 두 값이 같은 경우
# 같은 그 값을 도출해야 하기 때문에 두 가지 경우로 나눔
elif dice[0] == dice[1] or dice[1] == dice[2]:
    p = 1000 + dice[1] * 100
elif dice[0] == dice[2]:
    p = 1000 + dice[2] * 100
# 3. 세 값이 모두 다른 경우
# 위에서 전부 걸러지고 남은 경우.
# 리스트 메소드 max()를 사용해 최댓값을 도출
else:
    p = max(dice)*100

print(p)

# max()의 매개변수로 int를 여러개 줬을 때 함수가 돌아간다!?
# 본래 int는 iterable하지 않은 객체라서 max()함수의 매개변수로 줄 경우 오류가 난다.
# 이 방법대로 한다면

# 입력값을 받아 변수에 할당
a, b, c = map(int, input().split())

# 1. 세 값이 모두 같은 경우
if a == b and b == c:
    p = 10000 + a * 1000
# 2. 두 값이 같은 경우
# 같은 그 값을 도출해야 하기 때문에 두 가지 경우로 나눔
elif a == b or b == c:
    p = 1000 + b * 100
elif a == c:
    p = 1000 + c * 100
# 3. 세 값이 모두 다른 경우
# 위에서 전부 걸러지고 남은 경우.
# 메소드 max()를 사용해 최댓값을 도출
else:
    p = max(a, b, c) * 100

print(p)