import sys
# 전체 학생 명부
students = [0] * 30

for i in range(30):
    students[i] = i + 1

# 제출하지 않은 학생만 남기기
# 처음엔 그냥 for문 끝나고 중복제거하려 했으나 실패하여 애초에 for문에서 중복 걸러서 넣는 방법으로
for j in range(28):
    sub = int(sys.stdin.readline().strip())
    if sub in students:
        students.remove(sub)

# 1,2번째로 작은 애들 출력
students.sort()
print(students[0], students[1], sep='\n')