# 문제에서 주어진 조건대로 구현
# 처음에는 단순 정렬이라고 생각했지만 단순히 정렬하면 안됨
# 문제 조건대로 본인보다 덩치가 큰 사람의 수를 구하면 됨, 2중 for문 사용

import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)] # 사람들의 키와 몸무게를 입력받음

result = [] # 덩치 등수를 저장할 리스트
for i in range(n):
  rank = 1
  for j in range(n):
    if info[i][0] < info[j][0] and info[i][1] < info[j][1]: # 본인보다 덩치가 큰 사람이 있다면
      rank += 1 # count 
  
  result.append(rank) # rank result에 append

print(*result) # 최종 덩치 등수 출력
