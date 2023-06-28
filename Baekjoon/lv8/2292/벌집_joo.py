# 메모리: 31256 KB, 시간: 44 ms
 

import sys

N = int(sys.stdin.readline())

# N이 1인 경우
if N == 1:
    print(1)
else:
    cnt = 1  # 지나가는 하는 방의 개수
    room = 2  # 현재 방 번호

    #벌집의 방 번호가 N보다 작거나 같을 때까지만 반복한다.
    while room <= N:
        room += 6 * cnt #다음 벌집까지 방 번호를 구하기 위해 6을 곱하고 cnt를 더해준다.
        cnt += 1
        # print(room, cnt)

    print(cnt)