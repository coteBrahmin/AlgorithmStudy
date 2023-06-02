import sys

#처음엔 리스트로 하다가, 딕셔너리 방법을 시도하였는데
#딕셔너리는 키-값 순서를 잘 활용하는 게 중요한 것 같습니다.

nums = {0: i for i in range(1, 10)}

#몇번 째 줄인지를 value, input 값을 key로 넣어주고 최댓값을 뽑아줍니다.
# {0: 9, 3: 1, 29: 2, 38: 3, 12: 4, 57: 5, 74: 6, 40: 7, 85: 8} 이런 형태가 됩니다.
for i in range(1, 10):
    num = int(sys.stdin.readline())
    nums[num] = i

max = max(nums.keys())
print(max)
print(nums[max])