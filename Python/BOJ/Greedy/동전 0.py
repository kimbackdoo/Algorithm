# 문제 조건에 큰 동전은 작은 동전에 배수라는 조건이 있으므로 그리디 알고리즘 적용 가능
# 입력받은 동전들 중 가장 큰 수로 나눈 몫을 카운드하고 순서대로 작은 동전의 몫을 카운트를 반복

# n, k = map(int, input().split())

# moneys = []
# for _ in range(n):
#   moneys.append(int(input()))

# moneys.sort(reverse=True)

# result = 0
# for money in moneys:
#   if k // money != 0: # 몫이 있다면
#     result += (k // money) # 가장 큰 수로 나눈 몫을 더해나감
#     k %= money # 나머지를 이용하여 필요한 동전의 개수를 구함

# print(result)

# 동전들은 오름차순 정렬되어 있으므로 for문에서 역순으로 반복하면 됨
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

answer = 0
for coin in coins[::-1]: # coins의 모든 요소 순회, 이때 역순으로 순회
  answer += (k // coin) # 개수 count
  k %= coin

print(answer)
