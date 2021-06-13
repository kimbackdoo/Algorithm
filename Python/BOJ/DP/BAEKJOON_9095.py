# f(n) = f(n-1) + f(n-2) + f(n-3)

t = int(input())
for _ in range(t):
  n = int(input())

  d = [0] * 11 # 각 경우의 수를 저장할 DP 테이블을 0으로 초기화
  d[1], d[2], d[3] = 1, 2, 4 # 초기 1, 2, 3의 경우의 수 저장
  for i in range(4, n+1):
    d[i] = d[i-1] + d[i-2] + d[i-3] # 점화식 실행

  print(d[n])
