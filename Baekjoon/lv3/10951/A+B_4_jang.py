# 반복문 안에서 입력받을 때 실행시간 단축을 위해 sys 임포트
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

# 구글링해서 해결한 문제
# EOF (End Of File) - 파일의 끝을 판단할 수 있는지?
# 반복 구간이 정해지지 않은 조건은 while문을 사용한다.
# while문을 빠져나올 조건을 걸 때 if문을 사용하게 되면,
# 해당 문제와 같이 입력이 없는 상황에서는 그냥 에러가 나버린다.
# 따라서 try-except문으로 예외처리 해준다.
# 예외 발생시(입력이 끝나면) while문 탈출
