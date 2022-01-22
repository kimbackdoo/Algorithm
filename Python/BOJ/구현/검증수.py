# 문제 조건대로 구현하면 됨
# map 함수와 lambda 식 이용
import sys
input = sys.stdin.readline

# 입력을 받는대로 lambda식을 적용하여 제곱수로 만들고 sum 함수를 이용하여 입력받은 수들의 제곱 수들의 합을 구하고 10으로 나눈 나머지 출력
print(sum(map(lambda x: int(x) ** 2, input().split())) % 10)
