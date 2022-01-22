# 버튼을 누르는 횟수를 최소화하기 위해서는 A, B, C 순서대로 누르면 됨, 그리디, 구현 알고리즘
t = int(input())

# if t % 10 == 0: # 입력받은 시간이 나누어 떨어지면 버튼을 누름
#   times = [300, 60, 10]
#   answer = [0, 0, 0]
#   for i in range(3): # A부터 차례대로 버튼을 누름
#     answer[i] = t // times[i]
#     t %= times[i]
#   print(*answer)
# else: # 나누어 떨어지지 않으면 -1 출력
#   print(-1)

# 리스트로 만들지 않고, 한번에 계산
t = int(input())

if t % 10 == 0:
  print(t // 300, (t % 300) // 60, (t % 300 % 60) // 10)
else:
  print(-1)
