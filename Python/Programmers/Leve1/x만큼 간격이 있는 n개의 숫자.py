# def solution(x, n):
#     answer = []
#     num = 1
#     while len(answer) != n:
#         answer.append(x * num) # x부터 시작해서 x씩 증가
#         num += 1
        
#     return answer

def solution(x, n):
    return [(i+1) * x for i in range(n)] # 길이가 n 이어야 하므로 n번 반복하면서 x씩 증가하게 함
