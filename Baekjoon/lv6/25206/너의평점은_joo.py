# 메모리: 31256 KB, 시간: 44 ms
import sys

total_grade = 0
total_credit = 0
grade_dict ={"A+": 4.5, "A0":4, "B+":3.5, "B0": 3, "C+":2.5, "C0": 2,"D+":1.5, "D0":1, "F":0}

for _ in range(20):
        name, credit, grade = sys.stdin.readline().split()

        grade = list(grade)

        #P인 경우에는 등급과 학점 계산에서 모두 제외되어야한다.
        if "P" in grade:
            grade.remove("P")
            credit = 0
        
        else:
            total_credit += int(float(credit))  # 소수점 없애기 위한 float
            grade = "".join(grade)
            total_grade += float(grade_dict.get(grade)) * float(credit)

#total_credit 전체 수강 학점
#total grade = 학점 * 과목의 평점
#전공평점 = total grade / 전체 학점
print(f"{total_grade / total_credit:.6f}")


#학점 * 평점에서 전체를 나눠야 했다. 