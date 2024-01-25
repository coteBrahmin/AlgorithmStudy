n = int(input())
score = list(map(int, input().split()))

m = max(score)

for i in range(n):
        score[i] = score[i] / m * 100

print(sum(score) / n)

# for문 돌 때 range로 해서 score[i]로 하면 되는데
# 그냥 리스트의 요소들을 for문돌면 안되는 이유가 뭘까?
# 변수가 아니라 값처럼 취급되어서 그런건지?