# 무조건 첫 번째 도시에서 2번째 도시로 가야하기 때문에 첫 번째 도시의 비용을 저장해서 다음 도시의 비용과 비교해서 계산

# n = int(input())
# distance = list(map(int, input().split()))
# cost = list(map(int, input().split()))

# min = cost[0] # 첫번째 도시의 비용 저장
# result = distance[0] * cost[0] # 첫번째에서 2번째 도시로 무조건 가야하기 때문에 비용 저장
# for i in range(1, n-1): # 1번부터 n-1번 도시까지 반복, 이유는 마지막 도시는 생각할 필요 없기 때문
#   if min > cost[i]: # min의 저장된 값보다 다음 도시의 비용이 작으면
#     min = cost[i] # min 값 변경
#   result += min * distance[i] # 비용 계산

# print(result)

# 오랜만에 풀어서 그런지 풀이를 생각하는데 한참 걸림,,
# 그리디 사고력을 더 기를 필요가 있음
# 그리디 알고리즘은 해당 경우를 택할건지 안택할건지 순간순간마다 최적의 해를 구해야 함
# 따라서 주유소 문제는 해당 주유소의 가격이 저장된 최소값보다 작은지 큰지에 따라 순간순간 결정하면 됨
# 아래와 같이 풀수도 있으나 필요없는 변수와 조건문이 있으므로 위에 코드가 더 깔끔함

import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

result, tmp, min_price = 0, road[0], price[0]
for i in range(1, n - 1):
  if price[i] < min_price: # 현재 주유소의 가격이 저장된 최소값보다 작으면
    result += (min_price * tmp)
    min_price = price[i] # 최소값 갱신
    tmp = road[i]
  else:
    tmp += road[i]

result += (min_price * tmp)
print(result)
