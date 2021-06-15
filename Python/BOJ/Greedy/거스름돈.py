# 동전들이 모두 배수이므로 그리디 알고리즘
# 거스름돈의 최소 개수를 구하기 위해 제일 큰 동전부터 count

n = int(input())
k = 1000 - n

moneys = [500, 100, 50, 10, 5, 1]
result = 0
for money in moneys:
  if k // money != 0: # money로 나누었을때 몫이 0이 아니면
    result += (k // money) # result에 몫을 더해나감
    k %= money # 다음 동전의 개수를 구하기 위해 나머지 연산을 이용 

print(result)
