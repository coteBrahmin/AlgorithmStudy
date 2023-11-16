###인풋값을 받아온다.
A,B= map(int, input().split())
C = int(input())

#B+C를 60으로 나누어서 몫을 H(시간), 나머지를 M(분)으로 넣어준다.
H = (B+C)//60
M = (B+C)%60

#A+H가 23보다 작으면 그냥 A+H시 M분으로 하고
# 23보다 크다면 24를 빼줘서 형식을 맞춰준다.
#참고. 들여쓰기에 주의하자.
if A+H <= 23:
    print(A+H, M)
else:
    print(A+H-24, M)