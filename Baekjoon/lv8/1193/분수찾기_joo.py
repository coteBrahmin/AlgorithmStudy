# 메모리: 31256 KB, 시간: 48 ms

#방법1) 이진탐색
import sys

X = int(sys.stdin.readline())

low = 1 #분수의 범위의 최소값
high = X #분수의 범위의 최대값
result = 0 #대각선 번호, 초기값 0으로 설정

#이진 탐색을 통해 대각선 범위 찾기
#low가 high보다 작거나 같은 동안 반복
while low <= high:
    mid = (low + high) // 2 #대각선이 가진 분수의 개수

    # mid가 가진 대각선 개수가 X보다 크거나 같다면
    # result를 mid로 갱신하고 high를 mid -1로 조정
    # 대각선 번호를 좌측으로 이동시키는 것
    if mid * (mid + 1) // 2 >= X:
        result = mid
        high = mid - 1
    #그렇지 않으면 low를 조정하여 범위를 좁힘
    else:
        low = mid + 1


#대각선 번호 result에서의 위치힌 X의 상대적 위치
#대각선 번호 result에서 몇번째 분수인지
offset = X - result * (result - 1) // 2

#대각선 번호 짝수 번호인 경우/ 홀수 번호인 경우 다르게 계산하여 출력
#대각선 번호가 짝수 -> 분자(numerator)가 작아지고 분모(denominator)가 커지는 순서
#대각선 번호가 홀수 -> 분자가 커지고 분모가 작아지는 순서
if result % 2 == 0:
    numerator = offset
    denominator = result - offset + 1
else:
    numerator = result - offset + 1
    denominator = offset

print(f"{numerator}/{denominator}")



#방법2)
# import sys
#
# X = int(sys.stdin.readline())
#
# #대각선
# line =1
# while X > line:
#     X -= line
#     line +=1
#     # print(X, line)
#
#
# #대각선에 속하는 분자와 분모의 합이 짝수라면
# if line % 2 == 0:
#     mo = X
#     ja = line -  X + 1
# else:
#     mo = line - X + 1
#     ja = X
#
# print(mo,"/",ja, sep="")
