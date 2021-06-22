# 무조건 첫 번째 도시에서 2번째 도시로 가야하기 때문에 첫 번째 도시의 비용을 저장해서 다음 도시의 비용과 비교해서 계산

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min = cost[0] # 첫번째 도시의 비용 저장
result = distance[0] * cost[0] # 첫번째에서 2번째 도시로 무조건 가야하기 때문에 비용 저장
for i in range(1, n-1): # 1번부터 n-1번 도시까지 반복, 이유는 마지막 도시는 생각할 필요 없기 때문
  if min > cost[i]: # min의 저장된 값보다 다음 도시의 비용이 작으면
    min = cost[i] # min 값 변경
  result += min * distance[i] # 비용 계산

print(result)
