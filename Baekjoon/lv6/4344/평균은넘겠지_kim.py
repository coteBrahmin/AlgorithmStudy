#메모리 31256kb, 시간 48ms
T = int(input())
for _ in range(T):
    scores = list(map(int,input().split()))
    #학생수 N
    N = scores.pop(0)
    avg = sum(scores)/len(scores)
    #평균을 넘는 학생수 target
    target = 0
    for score in scores:
        if score > avg:
            target += 1
        else: continue
    #SQL에서 공부한 round(소수, 몇째짜리) 되더라구요? 쓸라다가 40.0% 때문에 검색..
    print(f"{format(target/len(scores)*100,'.3f')}%")