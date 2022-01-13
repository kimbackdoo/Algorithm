# 문제 요구사항대로 구현하면 되는 문제
# sys로 입력 받고, set으로 구현하여 시간초과 탈출
# set의 remove대신 discard 연산을 사용하여 해당 요소가 있으면 삭제하고, 없으면 continue
# all일 경우 미리 만들어둔 전체 집합을 사용, all 명령어가 나올 때마다 전체 집합을 생성하면 시간을 잡아먹음

# import sys

# m = int(sys.stdin.readline().rstrip())

# S = set() # 공집합
# all_set = set([str(i) for i in range(1, 21)]) # 전체 집합 생성
# for _ in range(m):
#   cmd = sys.stdin.readline().rstrip().split() # sys 입력으로 빠르게 입력받음
  
#   if cmd[0] == "add":
#     S.add(cmd[1])
#   elif cmd[0] == "remove":
#     S.discard(cmd[1])
#   elif cmd[0] == "check":
#     print(1 if cmd[1] in S else 0)
#   elif cmd[0] == "toggle":
#     if cmd[1] in S:
#       S.remove(cmd[1])
#     else:
#       S.add(cmd[1])
#   elif cmd[0] == "all":
#     S = all_set
#   else:
#     S = set()

# 령어 딕셔너리를 미리 만들어두고 꺼내씀, 가독성 증가
# all 명령어 일때는 미리 만들어두고 써야 시간 절약됨

import sys
input = sys.stdin.readline

s = set()
all_set = set(map(str, range(1, 21))) # all 명령어
command = { # command 딕셔너리
  "add": lambda x: s.add(x),
  "remove": lambda x: s.discard(x),
  "check": lambda x: print(1 if x in s else 0),
  "toggle": lambda x: s.discard(x) if x in s else s.add(x),
  "all": lambda: all_set,
  "empty": lambda: set()
}

m = int(input())
for _ in range(m):
  c = input().strip().split()
  # c의 길이에 따라 command 딕셔너리 호출
  if len(c) == 1: s = command[c[0]]()
  else: command[c[0]](c[1])
