# 세 방법 전부 동일
# 메모리 31256kb
# 시간 44ms

word = input()

# # 방법 1
# if "".join(reversed(word)) == word:
#     print(1)
# else:
#     print(0)

# # 방법 2
# if word[::-1] == word:
#     print(1)
# else:
#     print(0)

# 방법 3 - 투 포인터
left = 0
right = len(word)-1
is_p = 1
while left < right:
    if word[left] == word[right]:
        left += 1
        right -= 1
        continue
    else:
        is_p = 0
        break
        
print(is_p)