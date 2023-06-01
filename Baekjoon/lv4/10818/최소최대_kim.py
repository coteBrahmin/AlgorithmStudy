#첫 번째 풀이 (656ms, 97B)
N = int(input())
nums = list(map(int,input().split()))
#리스트 정렬을 해서
nums.sort()
#인덱스 0이 제일 작은수, 인덱스 -1이 제일 큰 수
print(f"{nums[0]} {nums[-1]}")

#두 번째 풀이 (368ms, 88B)
N = int(input())
nums = list(map(int,input().split()))
#굳이 sort를 할 필요없이 걍 min/max함수 곧장 씀
print(f"{min(nums)} {max(nums)}")

#세 번째 풀이 (360ms, 112B)
import sys
N = int(input())
#input()대신 sys.stdin.readline()적용해봄, 8ms 단축
nums = list(map(int,sys.stdin.readline().split()))
print(f"{min(nums)} {max(nums)}")

#시간은 8ms단축했는데 코드 크기는 24B늘어남
#시간복잡도랑 공간복잡도 더 자세히 알아야 어떤걸 선택할지 고를 수 있을듯
