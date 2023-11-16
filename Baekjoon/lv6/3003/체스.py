#31256KB, 44ms
#input값을 chess 리스트에 담아줍니다.
#체스 피스를 perfect_set으로 리스트를 만들었습니다.
#그리고 chess 리스트의 길이 만큼 perfect_set에서 빼주고 이를 출력합니다.

import sys

chess = [int(i) for i in list(sys.stdin.readline().split())]

perfect_set = [1, 1, 2, 2, 2, 8]

for i in range(0, len(chess)):
    perfect_set[i] -= chess[i]

print(*perfect_set)

#파이썬 리스트의 문자들을 숫자로 변환하는 방법 알아두기
