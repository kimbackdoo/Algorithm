#  a, b의 값을 각각 //2 연산을 반복해서 진행하고 a, b의 차가 1일 경우 stop
# a, b 중 큰 수가 홀수일 경우 a, b의 차가 1이지만 해당 라운드에서 만나는 것이 아니므로 예외 처리
# ex) a = 2, b = 3 일 경우, a, b의 차가 1이지만 1라운드가 아닌 2라운드에서 만남

# def solution(n, a, b):
#     answer = 1
#     while True:
#         if abs(a-b) == 1 and max(a, b) % 2 == 0: # 위 아이디어 대로 a, b의 차가 1이고 a, b 중에 큰 수가 짝수일 경우만 확인
#             break
#         # a, b가 짝수이면 //2, 홀수이면 //2 + 1을 진행
#         if a % 2 == 0: a //= 2 
#         else: a = a//2 + 1
            
#         if b % 2 == 0: b //= 2
#         else: b = b//2 + 1
            
#         answer += 1

#     return answer

def solution(n ,a, b):
    answer = 0
    while a != b: # a, b가 같지 않을 때까지
        answer += 1
        a, b = (a+1)//2, (b+1)//2 # 짝수, 홀수 구분없이 +1 한 값에 //2 연산을 진행하면 다음 라운드 번호가 나옴
        
    return answer
