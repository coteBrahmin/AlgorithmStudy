#메모리 31256kb 실행시간 44ms
#리스트로 인풋을 받고, 원래 있어야 하는 개수 리스트와 비교하는 방식으로 접근
pieces = list(map(int,input().split()))
correct = [1,1,2,2,2,8]
ans = []
for i in range(6):
    #원래 있어야 하는 개수에서 현재 인풋값을 빼야 필요한 만큼의 갯수가 나옴
    ans.append(correct[i] - pieces[i])
print(*ans)