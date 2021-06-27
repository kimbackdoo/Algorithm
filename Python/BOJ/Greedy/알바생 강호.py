# 원래 주려고 생각했던 돈이 제일 높은 사람을 제일 먼저 커피를 받게 하면 됨, 그리디 알고리즘 적용

n = int(input())
tips = [int(input()) for _ in range(n)]

result = 0
for idx, tip in enumerate(sorted(tips, reverse=True)): # 정렬한 후 (index+1)이 커피를 받는 순서이므로 enumerate 사용하여 idx, tip 추출 
  t = tip - idx # 팁 계산
  if t < 0: # 주려는 팁이 음수이면 0
    t = 0
  result += t

print(result)
