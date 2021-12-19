# ., X로 이루어진 보드판에서 .을 제외하고 AAAA 또는 BB로 모두 덮어야함
# 덮었을 때 사전순으로 가장 앞서는 답을 출력해야 하므로 AAAA가 덮일 수 있으면 AAAA 먼저 덮어야함, 그리디 알고리즘 적용

# board = input().replace("XXXX", "AAAA").replace("XX", "BB") # AAAA 먼저 덮고, BB를 덮음
# print(-1 if "X" in board else board) # 모두 덮어지지 않은 경우 -1, 덮어졌으면 board 출력

board = input()

# A로 먼저 덮고, B를 덮는 함수
# 예를 들어 XXXXXX 이면 l은 6이고, "A" * 4 * (6 // 4) + "B" * (l % 4)으로 A 먼저 덮고 B를 덮을 수 있음
def convert(l):
  return ("A" * 4 * (l // 4) + "B" * (l % 4)) if not l % 2 else -1 # l 만큼 모두 덮을 수 있으면 덮은 결과, 덮을 수 없으면 -1 return

result = ""
l = 0
for b in board:
  if b == "X":
    l += 1 # X의 길이 구함
  else:
    tmp = convert(l) # 덮은 문자열로 변환
    result += ("" if tmp == -1 else (tmp + b)) # l 만큼 덮지 못하였으면 "", 덮었으면 tmp + "."을 result에 더함
    l = 0 # l 초기화

tmp = convert(l) # 남은 문자열에 대한 길이에 대해 덮은 문자열로 변환
result += ("" if tmp == -1 else tmp) # l 만큼 덮지 못하였으면 "", 덮었으면 tmp을 result에 더함
print(result if len(result) == len(board) else -1) # result와 board의 길이가 같으면 result, 다르면 -1 출력
