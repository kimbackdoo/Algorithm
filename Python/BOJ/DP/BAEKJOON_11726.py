# f(n) = f(n-1) + f(n-2)

n = int(input())

d = [0] * 1001 # 경우의 수를 저장할 DP 테이블
d[1], d[2] = 1, 2 # 초기 1, 2의 경우의 수를 저장
for i in range(3, n+1):
  d[i] = (d[i-1] + d[i-2]) % 10007 # 점화식 실행

print(d[n])
