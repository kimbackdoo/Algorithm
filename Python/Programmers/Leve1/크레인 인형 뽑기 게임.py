def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][move-1])
                # 중복되는 코드 항상 줄이는 연습!
                board[i][move-1] = 0
                break
    
    return answer * 2
