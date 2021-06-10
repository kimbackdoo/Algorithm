# def solution(left, right):
#     answer = 0
#     for num in range(left, right+1):
#         cnt = 0
#         for i in range(1, num+1): # 1 ~ num까지 약수의 개수를 구함
#             if num % i == 0: # 약수면
#                 cnt += 1 # count
#         if cnt % 2 == 0: # 짝수면 더하고
#             answer += num
#         else: # 홀수면 뺄셈
#             answer -= num
    
#     return answer

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if int(num**0.5) == num**0.5: # num이 제곱근이 정수이면 약수의 개수는 홀수
            answer -= num
        else:
            answer += num

    return answer
