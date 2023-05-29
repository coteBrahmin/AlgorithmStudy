##방법1.
#2줄의 input을 각각 A,B에 넣어준다.
A = int(input())
B = int(input())

#B의 10의 자리, 100의자리, 1000의 자릿수가 필요하기 때문에 for문 사용해서 자릿수별 분리
#B의 10/100/1000으로 나눈 나머지의 몫을 계산하여 자릿수를 구하는 방법
for i in [10, 100, 1000]:
    print(int(A * (B % i // (i / 10 ))))

print(A*B)

##방법2.
#for 문을 통해 문자로 받아온 B의 자릿수별 숫자를 가져온다.
#string값이어야 하기 때문에 B는 스트링으로 받아왔고, 역순으로(2,1,0) 설정하여 자릿수를 받아온다.
A = int(input())
B = input()

for i in reversed(range(0,3)) :
   print(A*int(B[i]))

print(A*int(B))

#역순으로 할거면 숫자도 역으로 줘라.
for i in range(3,0,-1):
    print(i)