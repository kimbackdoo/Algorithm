# 주어진 수가 앞뒤가 똑같은지 확인하면됨
# 따라서 주어진 수를 문자열로 입력받고 역순과 같은지 확인하면됨
import sys
input = sys.stdin.readline

while True:
  n = input().strip()
  if n == "0": break
  # n과 n[::-1]이 같은지 확인
  print("yes" if n == n[::-1] else "no")
