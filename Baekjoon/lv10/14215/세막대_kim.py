#memory 31120kb, time 44ms
import sys
tri_lens = list(map(int,sys.stdin.readline().split()))
#sum-max는 두 변의 합
if sum(tri_lens)-max(tri_lens) <= max(tri_lens):
    #두 변의 합이 max변 보다 1만 크도록 max를 줄여야 삼각형 넓이가 가장 커짐
    tri_lens[tri_lens.index(max(tri_lens))] = sum(tri_lens)-max(tri_lens)-1
    print(sum(tri_lens))
else:print(sum(tri_lens))