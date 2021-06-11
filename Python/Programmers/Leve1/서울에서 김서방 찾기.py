# def solution(seoul):
#     idx = 0
#     for i in range(len(seoul)):
#         if seoul[i] == "Kim":
#             idx = i
            
#     return "김서방은 {}에 있다".format(idx)

# def solution(seoul):
#     answer = [i for i in range(len(seoul)) if seoul[i] == "Kim"]
#     return "김서방은 " + str(answer[0]) + "에 있다"

def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))
