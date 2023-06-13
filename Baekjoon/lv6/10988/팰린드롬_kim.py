#메모리 31256kb	실행시간 44ms
str = list(input())
for i in range(len(str)):
    #첫번째 인덱스와 마지막 인덱스 투 포인터로 비교
    #같지 않으면 0을 리턴하고 나머지 연산 하지 않고 for문 빠져나오기
    if str[i] is not str[-(i+1)]:
        print(0)
        break
    #같은 경우에는 마지막 포인터까지 간 뒤 최종적으로 1리턴
    elif i is len(str)-1:
        print(1)
    else:continue