# 메모리: 31388 KB, 시간: 44 ms
import sys

#ord() - 문자에 해당하는 아스키값을 반환

N, B = sys.stdin.readline().split()
sum = 0 #총합 = 0으로 초기화

#0부터(첫번째 값)부터 마지막 값까지 역순으로 반복
for i in range(len(N)-1,-1,-1):
    if N[i].isdigit(): 
        #N의 i번째 문자가 숫자일 경우,
        #N[i] * B^len(N)-i을 이용하여 진법 변환
        sum += int(N[i])*(int(B)**(len(N)-1-i))

        #알파벳 대문자인 경우,
        #ord()를 이용하여 A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35로 치환하여 진법 변환
    elif 64 <= ord(N[i]) <= 91:
         sum += ((ord(N[i])-55) * (int(B)**(len(N)-1-i)))

print(sum)