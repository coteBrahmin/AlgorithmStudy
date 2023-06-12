T = int(input())
for _ in range(T):
    #N = ['3','ABC']
    N = input().split()
    #str = ['A','B','C']
    str = list(N[1])
    ans = []
    for i in str:
        ans.append(i*int(N[0]))
    print(*ans,sep='')