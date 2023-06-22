#메모리 31256kb,시간 40ms
import sys
T = int(sys.stdin.readline())
#동전 단위를 센트로 환산한 리스트
charge = [25, 10, 5, 1]
for _ in range(T):
    #거슬러줄 동전의 값어치를 key, 동전 개수를 value로 하는 딕셔너리
    return_charge = {25: 0, 10: 0, 5: 0, 1: 0}
    price = int(sys.stdin.readline())
    for i in charge:
        #몫이 없을 땐 더 작은 단위 동전으로 이동
        if price//i == 0:
            continue
        else:
            #가격을 현재 동전 단위로 나눈 몫이 현재 동전의 개수가 된다
            return_charge[i] = price//i
            #나머지가 없는 경우 이미 계산이 끝났으므로 바로 for문 빠져나오기
            if price//i == 0:
                break
            #가격을 현재 동전 단위로 나눈 나머지가 다음 동전 단위의 대상이 된다
            else: price = price%i
    print(*return_charge.values())