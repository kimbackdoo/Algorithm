# 주어진 실수들을 현재 값과 연속해서 곱한 값의 최대값을 비교하면 연속부분최대곱을 구할 수 있음
# 예를 들어, 1.1, 0.7, 1.3, 0.9, 1.4, 0.8, 0.7, 1.4가 있으면 max(0.7, 1.1 * 0.7) = 1.1 * 0.7 = 0.77, max(1.3, 1.3 * 0.77) = 1.3, ...
# 즉, f(i) = max(f(i), f(i) * f(i-1))이 됨

import sys
input = sys.stdin.readline

n = int(input())
numbers = [float(input()) for _ in range(n)] # 실수이기 때문에 float으로 형변환, 파이썬에서는 double가 없고 float이 double과 같음

for i in range(1, n):
  numbers[i] = max(numbers[i], numbers[i] * numbers[i-1]) # 위 점화식을 적용하여 연속부분의 최대곱을 구함

print("{:.3f}".format(max(numbers))) # 출력에 소수점 이하 셋째 자리까지 출력하라고 했으므로 서식을 지정해야 함, {:.3f}.format()을 이용하여 소수점 이하 셋째 자리까지 출력
