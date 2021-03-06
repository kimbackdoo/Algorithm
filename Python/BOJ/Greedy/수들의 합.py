# 가장 작은 수부터 차례대로 비교해나가므로 그리디 알고리즘
# 문제에서 요구하는 것이 서로 다른 N개의 자연수의 합이 s가 될 때, N의 최대값을 구하는 것이므로
# s를 1부터 차례대로 뺄셈해나가면 된다 이때, s가 음수가 되는 순간이 N의 최대값이 됨
# 즉, s가 200이면, 1 ~ 20까지의 합 = 210에서 10을 빼면 되는 것이므로 19개가 됨

s = int(input())

n = 1
while True:
  s -= n
  if s < 0: break # s가 음수가 되는 순간 break
  n += 1

print(n-1) # 최종 n-1이 최대 N의 개수가 됨
