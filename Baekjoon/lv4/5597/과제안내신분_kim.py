#총 학생 리스트
students = list(range(1,31))
for _ in range(28):
    N = int(input())
    #인풋을 받아서 총 학생 리스트에서 제거하고 출석 안한 애만 남기려 함 
    if N in students:
        #pop()안에는 "인덱스"가 들어가야 한다.. (그냥 N썼다가 삽질함)
        students.pop(students.index(N))
    else:continue
#총 학생 리스트는 번호순으로 sort되어 있으니까 남은애 하나씩 프린트 하면 됨
print(students[0])
print(students[1])