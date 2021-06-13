# f(n) = f(n-1) + f(n-2)
# 0, 1의 호출 횟수도 위 점화식과 똑같이 호출됨

t = int(input())
for _ in range(t):
  n = int(input())

  d = [(1, 0), (0, 1)] # 초기 f(0), f(1)의 0, 1 호출 횟수를 저장
  for i in range(2, n+1):
    d.append((d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1])) # 점화식대로 0과 1의 호출 횟수를 각각 구하여 append

  print(d[n][0], d[n][1])
