# 입력, 출력에서 계속해서 시간 초과
# 파일명을 오른차순 정렬, 파일명이 같으면 입력받은 확장자 순, 파일 확장자 사전 순으로 정렬
# (파일명, 확장자, OS에서 인식하는 확장자) 튜플로 이루어진 리스트 생성후 파일명을 기준으로 파일명이 같다면 OS에서 인식하는 확장자를 기준으로 오름차순 정렬
# 이때 확장자가 OS에서 인식하는 확장자가 아니라면 확장자 앞에 "z"를 붙여 OS에서 인식하는 확장자가 앞으로 정렬되게 함

import sys
input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())

file = [0] * n
d = {} # OS에서 인식하는 확장자를 저장할 dict
for i in range(n):
  file[i] = input().split(".")
  d[file[i][1]] = "z" + file[i][1] # OS에서 인식하지 못하는 확장자는 확장자 앞에 "z"를 붙여 저장

ext = [0] * m
for i in range(m):
  ext[i] = input()
  d[ext[i]] = ext[i] # OS에서 인식하는 확장자라면 OS에서 인식하는 확장자로 저장

for f in file:
  f.append(d[f[1]]) # (파일명, 확장자, OS에서 인식하는 확장자) 튜플로 리스트 생성

for f in sorted(file, key=lambda x: (x[0], x[2])): # 1차적으로 파일명을 기준으로 정렬, 파일명이 같다면 2차적으로 OS에서 인식하는 확장자를 기준으로 정렬
  output(f'{".".join(f[:2])}')
