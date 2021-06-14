# f(0) = 0, f(1) = 1
# f(n) = f(n-1) + f(n-2)

n = int(input())

d = [0] * (n+1) # 피보나치 수를 저장할 DP 테이블
if n > 0: # n이 0일 경우도 있으므로 예외 처리
  d[1] = 1
  for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2] # 점화식 실행

print(d[n])
