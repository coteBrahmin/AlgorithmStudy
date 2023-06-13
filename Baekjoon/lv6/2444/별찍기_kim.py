#메모리 31256kb	실행시간 40ms
N = int(input())
#i는 1부터 2i까지 2i-1개
for i in range(1,2*N+1):
    #i가 N보다 작은 경우 *i = N-1, Ni = 2i-1
    if i <= N: print(' '*abs(N-i)+'*'*(2*i-1))
    #i가 N보다 큰 경우 *i = -(N-1), Ni = 2(2N-i)-1
    else: print(' '*abs(N-i)+'*'*(2*(2*N-i)-1))