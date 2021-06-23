# answer에 매번 타고 내린 사람의 수를 누적해서 append

answer = []
result = 0
for _ in range(4):
  minus, plus = map(int, input().split())

  result += (plus - minus)
  answer.append(result)

print(max(answer))
