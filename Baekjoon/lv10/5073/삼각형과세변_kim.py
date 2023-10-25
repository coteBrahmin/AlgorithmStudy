#memory 31120kb, time 40ms
import sys
while True:
    tri_lens = list(map(int,sys.stdin.readline().split()))
    if sum(tri_lens) == 0: break
    else:
        if sum(tri_lens)-max(tri_lens) > max(tri_lens):
            if tri_lens[0] == tri_lens[1] == tri_lens[2] : print('Equilateral')
            #이거 너무 js틱한.. 느낌인데 다른 방식 없을랑가요
            elif tri_lens[0] == tri_lens[1] or tri_lens[0] == tri_lens[2] or tri_lens[1] == tri_lens[2]: print('Isosceles')
            else:print('Scalene')
        else:print("Invalid")