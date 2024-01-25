import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    ans = ''
    for a in S:
        ans += a*int(R)
    print(ans)

# 반복할 횟수와 단어를 문자열로 받는다.
# 빈 문자열 ans를 선언하고, for문으로 단어를 돌며 각 문자를 R번 곱하여 ans에 더한다