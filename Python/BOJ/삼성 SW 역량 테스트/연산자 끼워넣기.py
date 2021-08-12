# 주어진 연산자의 모든 경우를 확인해야함
# permutations 모듈을 이용하여 만들 수 있는 모든 경우를 구하고 해당 경우에 따라 최대값, 최소값을 찾음
# "+++*//", "+++//*"인 경우는 생각하면 "+++"인 값이 겹치게 되지만 permutations 모듈을 이용하면 겹치는 값들도 다시 계산하는 문제가 있음
# 값을 미리 기억해두는 백트래킹 알고리즘 공부 필요

import sys
input = sys.stdin.readline

from itertools import permutations

def operation(op, a, b): # 연잔사에 따른 결과값을 return
  if op == "+":
    return a + b
  elif op == "-":
    return a - b
  elif op == "*":
    return a * b
  else:
    if a < 0:
      return -(-a // b)
    else:
      return a // b

n = int(input())
numbers = list(map(int, input().split()))

op = []
for idx, cnt in enumerate(list(map(int, input().split()))): # 입력받은 연산자의 개수에 따라 연산자를 구함, 예를 들어, ["+", "+", "-", "*", "//"]
  op.extend(["+-*//"[idx]] * cnt)

mx, mn = -1e9, 1e9 # 문제에서 최소 -10억, 최대 10억이라고 했으므로 최소, 최대값 설정, 1e9는 10 ** 9 즉, 10억을 의미
for p in set(permutations(op, n - 1)): # permutations 모듈을 이용하여 만들 수 있는 모든 경우를 구함
  total = numbers[0] # 첫번째 값 고정
  for i in range(n-1):
    total = operation(p[i], total, numbers[i+1]) # 각 경우마다 값을 구함
  
  # 최대, 최소 값 구함
  if mx < total: mx = total
  if mn > total: mn = total

print(mx)
print(mn)
