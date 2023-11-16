import sys

students = list(range(1,31)) #출석번호 1~30번까지 리스트를 만들어줍니다.

#인풋값 -> 출석으로 간주하여 해당 학생 번호는 remove합니다.
#이미 리스트가 정렬되어 있어서 그냥 출력해줍니다.
for i in range(1,29):
    check = int(sys.stdin.readline())
    students.remove(check)

print(*students)

#리스트 요소 삭제 정리 :
# 리스트.remove(값) => student.remove(check)
# 리스트.pop(인덱스) => student.pop(student.index(check))
# del 리스트[인덱스] => del student[student.index(ckeck)]
