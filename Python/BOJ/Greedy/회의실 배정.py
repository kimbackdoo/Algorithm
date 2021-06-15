# 회의 끝나는 시작이 제일 짧은 것을 선택하면 최대한 많은 회의를 할 수 있으므로 그리디 알고리즘
# 시작시작, 끝 시간 입력 받은 후 끝 시간과 시작 시간의 순서를 바꾸어 time 리스트에 append
# 끝 시간 기준으로 오름차순 정렬 이때 끝 시간이 같을 경우 시작시간으로 오름차순 정렬됨

import sys

n = int(input())

time = []
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  a, b = b, a
  time.append([a, b]) # 시작, 끝 시간 순서를 바꾸어 time 리스트에 append

time.sort() # 끝 시간 기준 오름차순 정렬, 끝 시간이 같다면 시작 시간 기준 오름차순 정렬

result = 0
tmp = [time[0]]
for i in range(1, len(time)):
  if tmp[-1][0] <= time[i][1]: # tmp[-1]의 끝 시간보다 다음 시작 시간이 크거나 같다면 회의실 사용 가능
    tmp.append(time[i]) # 따라서 append

result = len(tmp) # tmp의 길이가 회의실을 사용할 수 있는 최대 개수
print(result)
