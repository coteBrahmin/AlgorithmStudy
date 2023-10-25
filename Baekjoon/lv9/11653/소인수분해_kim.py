#memory 31120kb, time 1520ms
import sys
N = int(sys.stdin.readline())
temp = N
i = 2
if N != 1:
    #temp가 소수이면 끝내고 싶은데 while문의 조건식을 for문으로 만들순 없어서 그냥 최소의 소수인 2로 일단 정함..
    while temp >= 2:
        if temp % i == 0:
            temp /= i
            print(i)
        else: i += 1