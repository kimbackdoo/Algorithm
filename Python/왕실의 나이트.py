# ord : 문자를 아스키코드 값으로 바꾸는 내장함수

def solution(position):
  x = ord(position[0]) - ord('a') + 1
  y = int(position[1])

  moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
  answer = 0
  for move in moves:
    if (x + move[0]) >= 1 and (x + move[0]) <= 8:
      if (y + move[1]) >= 1 and (y + move[1]) <= 8:
        answer += 1

  return answer
