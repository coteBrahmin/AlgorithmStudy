#일단 입력값이 들어간 numlist 생성
numlist = []

for i in range(2):
    numlist.append(input())

#첫 번째 숫자를 두 번째 숫자의 1의자리~3의자리까지 곱하는 것이기 때문에 
# 두 번째 숫자의 자릿수별로 자른 second 리스트를 생성
second = list(numlist[1])

#첫 번째 숫자 * 두 번째 숫자의 1의자리
print(int(numlist[0])*int(second[2]))

#첫 번째 숫자 * 두 번째 숫자의 10의자리
print(int(numlist[0])*int(second[1]))

#첫 번째 숫자 * 두 번째 숫자의 100의자리
print(int(numlist[0])*int(second[0]))

#첫 번째 숫자 * 두 번째 숫자의 최종 결과
print(int(numlist[0])*int(numlist[1]))