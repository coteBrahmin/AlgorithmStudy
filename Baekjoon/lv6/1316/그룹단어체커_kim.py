#메모리 31256kb, 시간 48ms
import sys
T = int(sys.stdin.readline())
ans = 0
for _ in range(T):
    #단어를 리스트로 받은 뒤 인덱스를 통해 하나씩 탐색하면서 점검시도 
    str = list(sys.stdin.readline())
    #없으면 담고 있으면 넘어갈 체커리스트 
    checker = []
    for i in range(len(str)):
        #체커에 없으면 담는다 
        if str[i] not in checker:
            checker.append(str[i])
        else:
            #체커에 있는 경우 연속된 문자인지 확인
            if str[i] == str[i-1]:
                continue
            #연속된 문자가 아닌 순간 정답에서 뺀 후 for문 빠져나오기
            else:
                ans -= 1
                break
    #for문을 다 돌았으면 정답임
    ans += 1
print(ans)