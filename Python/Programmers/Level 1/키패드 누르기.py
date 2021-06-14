# def solution(numbers, hand):
#     keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
#               4: (1, 0), 5: (1, 1), 6: (1, 2),
#               7: (2, 0), 8: (2, 1), 9: (2, 2),
#               10: (3, 0), 0: (3, 1), 10: (3, 2),
#     }
    
#     answer = ""
#     left, right = 10, 10
#     for number in numbers:
#         if number in [1, 4, 7]:
#             left = number
#             answer += "L"
#         elif number in [3, 6, 9]:
#             right = number
#             answer += "R"
#         else:
#             x, y = keypad[number]
#             left_x, left_y = keypad[left]
#             right_x, right_y = keypad[right]
#             if abs(x-left_x) + abs(y-left_y) > abs(x-right_x) + abs(y-right_y):
#                 right = number
#                 answer += "R"
#             elif abs(x-left_x) + abs(y-left_y) < abs(x-right_x) + abs(y-right_y):
#                 left = number
#                 answer += "L"
#             else:
#                 if hand == "right":
#                     right = number
#                     answer += "R"
#                 else:
#                     left = number
#                     answer += "L"
                    
#     return answer

def distance(number, direction): # 중복되는 코드 피하기 위하여 반복되는 코드 함수로 분리
    keypad = {1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
                10:(3,0), 0:(3,1), 10:(3,2)}

    x_number, y_number = keypad[number]
    x_direction, y_direction = keypad[direction]

    return abs(x_number-x_direction) + abs(y_number-y_direction)

def solution(numbers, hand):
    answer = ''
    left, right = 10, 10
    for number in numbers:
        if number in [1,4,7]:
            answer += "L"
            left = number
        elif number in [3,6,9]:
            answer += "R"
            right = number
        else:
            if distance(number, left) == distance(number, right):
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number
            elif distance(number, left) < distance(number, right):
                answer += "L"
                left = number
            else:
                answer += "R"
                right = number

    return answer
