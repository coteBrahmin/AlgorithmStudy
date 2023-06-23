#메모리 31256kb, 시간 52ms
import sys
N = int(sys.stdin.readline())
#지그재그 라인의 endpoint를 항으로 하는 An = 직전항 + n
#직전항 (endpoint)
beforeAN = 1
#endpoint가 몇 번째 라인에 있는지 
count_n = 1
if N == 1 :
   print('1/1')
else:
    for n in range(2, N + 2):
        if N < beforeAN:
            #지그재그 요소들은 count_n번째 라인에 count_n 개 있으므로  
            #현재 beforeAN은 endpoint 점이다, 여기로부터 얼만큼 떨어져 있나
            one = beforeAN-N+1
            #반대방향으로는 얼만큼 떨어져 있나  
            theOther = count_n-one+1
            #짝수항은 endpoint가 y축에서 끝나고 홀수항은 x축
            if count_n%2 == 0:
                print(f"{theOther}/{one}")
            else:
                print(f"{one}/{theOther}")
            break
        else:
            AN = beforeAN + n
            beforeAN = AN
            count_n = n
            #같아지는 경우를 여기다 놓은 이유는 다음 턴으로 돌리면 n이 1증가 하기 때문인데 
            #똑같은걸 두번 쓴건 무언가 잘못된 것 같아서 추후 다른 방법 찾아볼 생각
            if N == beforeAN:
                one = beforeAN-N+1
                theOther = count_n-one+1
                if count_n%2 == 0:
                    print(f"{theOther}/{one}")
                else:
                    print(f"{one}/{theOther}")
                break