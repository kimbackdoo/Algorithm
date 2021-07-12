# 물이 샌 위치에서 좌우 0.5 간격을 테이프로 막아야 물이 안샘
# 좌우 0.5 간격 리스트의 모든 요소를 순회하면서 길이가 L인 테이프를 최소한으로 사용해야 함
# 즉, 길이가 L인 테이프로 최대한 많은 위치를 막아야 하므로 그리디 알고리즘

# n, l = map(int, input().split())
# locations = list(map(int, input().split()))

# leaks = set()
# # 물이 새는 위치의 모든 요소를 순회하면서 집합 leaks에 추가
# # leaks를 집합으로 선언한 이유는 좌우 간격 0.5을 계산할 때 중복될 수 있으므로
# for location in locations:
#   leaks.add(location - 0.5)
#   leaks.add(location + 0.5)

# leaks = sorted(leaks) # leaks 오름차순 정렬
# result, tmp = 0, leaks[0]
# for i in range(1, len(leaks)):
#   if leaks[i] - tmp > l: # leaks[i] - tmp 값이 l보다 크다면 즉, 길이가 l인 테이프로 막을 수 없다면
#     result += 1 # 사용할 테이프의 개수 +1 증가
#     tmp = leaks[i] # 테이프 1개를 사용했으므로 해당 위치를 tmp에 저장
# # 예를 들어, leaks = [0.5, 1.5, 2.5, 99.5, 100.5, 101.5]라면 99.5부터 테이프를 사용하지만 위 로직에 의하면 계산이 안됨
# print(result + 1) # 따라서 테이프의 개수를 +1 하여 마지막 테이프를 더함

# 단순하게, 물이 새는 위치에서 길이가 L인 테이프를 사용하여 최대한 붙이면 되므로 좌우 간격 0.5 집합을 따로 선언하지 않아도 됨
n, l = map(int, input().split())
location = sorted(map(int, input().split())) # 물이 새는 위치를 입력 받으면서 오름차순 정렬

result, tmp = 0, location[0] - 0.5 # -0.5를 하는 이유는 만약 위치 1에 길이가 2인 테이프를 붙이면 위치가 0.5 부터 막아야 하므로
for i in range(1, len(location)):
  if location[i] - tmp > l: # leaks[i] - tmp 값이 l보다 크다면 즉, 길이가 l인 테이프로 막을 수 없다면
    result += 1 # 사용할 테이프의 개수 +1 증가
    tmp = location[i] - 0.5 # 테이프 1개를 사용했으므로 해당 위치를 tmp에 저장
    
print(result + 1) # 마지막에 테이프를 사용하므로 테이프 개수 +1
