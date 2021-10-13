# 주어지는 1차 방정식들은 모두 교점을 하나씩만 가지고 있음, 문제에 나온 공식을 그대로 이용
# line을 모두 순회하면서 교점을 구함

# def solution(line):
#     x_coord, y_coord = [], [] # x, y의 좌표들을 저장할 리스트
#     for i in range(len(line)): # line의 모든 요소 순회
#         a, b, e = line[i]
#         for j in range(i + 1, len(line)): # 교점을 구하기 위해 i번째 요소를 제외한 나머지 모든 요소 순회
#             c, d, f = line[j]
#             if ((a * d) - (b * c)): # 공식 적용, 나눌때 분모가 0이 되면 안되기 때문에 예외 처리
#                 # 공식 적용
#                 x = ((b * f) - (e * d)) / ((a * d) - (b * c))
#                 y = ((e * c) - (a * f)) / ((a * d) - (b * c))
#                 if x == int(x) and y == int(y): # 공식을 적용한 x, y의 값이 정수이면
#                     # x, y의 값 각각 append
#                     x_coord.append(int(x))
#                     y_coord.append(int(y))

#     board = [] # 초기 격자판을 저장할 리스트
#     # 격자판은 모든 별을 포함한 최소 크기가 되어야 함
#     # 최소 크기는 y의 최대값, 최소값의 차, x의 최대값, 최소값의 차가 됨을 이용
#     for i in range(max(y_coord) - min(y_coord) + 1):
#         tmp = []
#         for j in range(max(x_coord) - min(x_coord) + 1):
#             tmp.append(".") # 초기 격자판 "."으로 설정

#         board.append(tmp)
    
#     # x, y의 좌표를 격자판의 인덱스로 변환해야함
#     # 좌측 최상단이 (0, 0)이므로 x 좌표는 리스트에서 최소값을 빼면 되고, y 좌표는 리스트에서 최대값을 빼면 됨
#     a, b = min(x_coord), max(y_coord)
#     for i in range(len(x_coord)):
#         x = abs(x_coord[i] - a)
#         y = abs(y_coord[i] - b)
#         board[y][x] = "*" # 변환한 좌표값에 해당하는 값을 "*"로 변경

#     answer = [] # 최종 결과값을 저장할 리스트
#     for item in board:
#         answer.append("".join(item)) # 정답에 맞게 변환

#     return answer

# def solution(line):
#     x_coord, y_coord = [], []
#     for i in range(len(line)):
#         a, b, e = line[i]
#         for j in range(i + 1, len(line)):
#             c, d, f = line[j]
#             # if문을 중첩하지 않고 분모가 0인지, 좌표값이 정수인지 한번에 확인
#             div = ((a * d) - (b * c))
#             if div and ((b * f) - (e * d)) % div == 0 and ((e * c) - (a * f)) % div == 0: # 분모가 0이 아니면서 좌표값이 정수면
#                 x = ((b * f) - (e * d)) // ((a * d) - (b * c))
#                 y = ((e * c) - (a * f)) // ((a * d) - (b * c))
#                 # 좌표값 저장
#                 x_coord.append(x)
#                 y_coord.append(y)
    
#     # 리스트 컴프리헨션을 이용하여 초기 격자판 설정
#     answer = [["."] * (max(x_coord) - min(x_coord) + 1) for _ in range(max(y_coord) - min(y_coord) + 1)]
    
#     a, b = min(x_coord), max(y_coord)
#     for i in range(len(x_coord)):
#         # y좌표는 최대값에서 i번째 요소를 빼면 되고, x좌표는 i번째 요소에서 최소값을 빼면 되므로 abs 함수 사용할 필요없음
#         answer[b - y_coord[i]][x_coord[i] - a] = "*"
    
#     return ["".join(row) for row in answer] # 리스트 컴프리헨션을 이용하여 정답 return

def solution(line):
    coords = set() # x, y의 좌표값을 따로 저장하지 않고 한번에 저장, 좌표값은 중복될 수 있으므로 set 이용
    # ((b * f) - (e * d)), ((e * c) - (a * f)) 값의 최소, 최대값은 -10e10, 10e10이므로 x, y의 최소, 최대값을 구하기 위한 초기값 설정
    maxX, minX, maxY, minY = -10e10, 10e10, -10e10, 10e10
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            div = (a * d) - (b * c)
            if div and ((b * f) - (e * d)) % div == 0 and ((e * c) - (a * f)) % div == 0:
                x = ((b * f) - (e * d)) // div
                y = ((e * c) - (a * f)) // div
                maxX, minX, maxY, minY = max(maxX, x), min(minX, x), max(maxY, y), min(minY, y) # x, y의 최소, 최대값을 구함
                coords.add((x, y)) # 좌표 저장
    
    answer = [["."] * (maxX - minX + 1) for _ in range(maxY - minY + 1)] # 리스트 컴프리헨션을 이용하여 초기 격자판 설정
    for x, y in coords:
        answer[maxY - y][x - minX] = "*" # 좌표를 격자판의 인덱스로 변환 후 해당 요소 "*"로 변환
    
    return ["".join(row) for row in answer] # 리스트 컴프리헨션을 이용하여 정답 return
