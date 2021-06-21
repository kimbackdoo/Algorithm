# 듣지도 보지도 못한 사람을 구하는 문제이므로 즉, 교집합을 구하면 됨

n, m = map(int, input().split())

hear = set()
for _ in range(n):
  hear.add(input())

see = set()
for _ in range(m):
  see.add(input())

answer = hear & see # 교집합 구하기
print(len(answer))
for name in sorted(answer): # 오름차순 정렬 후 
  print(name)
