# 0 과 1이 바뀌는 순간마다 0과 1의 개수를 count하여 최종 작은 수를 출력
# 0과 1 중 바뀌는 횟수가 적은 것이 정답이므로 그리디 알고리즘
# 예를들어, s가 0001011 이라면 0에서 1로 바뀌는 부분은 2번, 1에서 0으로 바뀌는 부분 1이지만 s의 마지막 요소 1 또한 바뀌는 부분으로 생각하여 총 2번이 됨
# 즉, 위 예시에서는 0에서 1로 바뀌는 부분 2, 1에서 0으로 바뀌는 부분 2로 같기 때문에 0, 1 둘 중에 아무거나를 선택해 2번 바꾸면 됨

# s = input()

# cnt = [0, 0] # 0, 1이 바뀌는 개수를 count할 리스트
# tmp = s[0]
# for i in range(1, len(s)):
#   if tmp != s[i]: # 모든 요소를 순회하면서 tmp와 s[i] 값이 다를 경우
#     if tmp == "0": # 0에서 1로 바뀐 경우, 0의 개수를 1 증가
#       cnt[0] += 1
#     else: # 1에서 0으로 바뀐 경우, 1의 개수를 1 증가
#       cnt[1] += 1

#     tmp = s[i] # 바뀔 때마다 tmp 값 수정

# # 위 예시와 같이 s의 마지막 요소도 생각해야 하므로 
# if s[-1] == "0": # 마지막 요소가 0이라면 0의 개수 1 증가
#   cnt[0] += 1
# else: # 마지막 요소가 1이라면 1의 개수 1 증가
#   cnt[1] += 1

# print(min(cnt))

s = input()
cnt = 0

# 바뀌는 지점 카운트
# 바뀌는 지점 개수가 짝수일 경우에는 cnt//2, 홀수일 경우에는 (cnt+1)//2 이므로
# 짝수, 홀수 상관없이 (cnt+1) // 2가 정답이 
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cnt += 1

print((cnt+1)//2)
