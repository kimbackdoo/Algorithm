# def solution(x, n):
#     answer = []
#     num = 1
#     while len(answer) != n:
#         answer.append(x * num) # x부터 시작해서 x씩 증가
#         num += 1
        
#     return answer

# def solution(x, n):
#     return [(i+1) * x for i in range(n)] # 길이가 n 이어야 하므로 n번 반복하면서 x씩 증가하게 함

def solution(x, n):
    # range 함수를 이용하여 숫자 범위를 만들고 리스트로 변환
    # 범위의 마지막 값을 x * (n + 1)로 하여 양수, 음수일때 처리되도록함
    # x가 0인 경우도 있으므로 0인 경우는 [0] * n을 return
    return list(range(x, x * (n + 1), x)) if x else [0] * n
