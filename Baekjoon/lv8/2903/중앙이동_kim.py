#메모리 31256kb, 시간 44ms
import sys
#점의 수는 4,9,25 ... => 2^2, 3^2, 5^2 제곱수의 형태로 증가
#그래서 2,3,5 단위로 수열 An 형성
#An은 첫째항 기준으로 1,3,7,15 ... 즉 2^n-1 만큼 증가
N = int(sys.stdin.readline())
#첫째항
A1 = 2
AN = A1 + (2**N-1)
print(AN**2)	