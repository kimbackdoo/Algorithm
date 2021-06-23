# 검은색, 하얀색 칸이 번갈아 표시되어 있고, (0, 0) 좌표가 하얀색 칸이므로 체스판에서 하얀색 칸은 좌표값의 합이 짝수인 경우에 해당

board = []
for _ in range(8):
  board.append(list(input()))

count = 0
for i in range(len(board)):
  for j in range(len(board[i])):
    if (i+j) % 2 == 0 and board[i][j] == "F": # 좌표의 합이 짝수이고 그 칸에 말이 있으면
      count += 1 # count

print(count)
