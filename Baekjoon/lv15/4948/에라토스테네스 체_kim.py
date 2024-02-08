import sys
stop = 1
while stop:
    N = int(sys.stdin.readline())
    if not N:
        stop = 0
    else:
        #인덱스와 수를 똑같이 맞추기 위해서 0부터 시작해 2n개 길이의 0배열을 만듦
        sieve = list(range(0,2*N+1))
        result = 0
        #소수는 2부터 시작하므로 2부터 탐색
        for i in range(2,2*N+1):
            if sieve[i] == 1:
                continue
            else:
                # n < result <= 2n 이 답이므로
                if i>N:
                    result += 1
                #1이 아닌 수(i)의 배수는 소수가 될수 없으므로 체에서 거른다.     
                for j in range(i,2*N+1,i):
                    if sieve[j] == 1:
                        continue
                    else:
                        sieve[j] = 1
        print(result)