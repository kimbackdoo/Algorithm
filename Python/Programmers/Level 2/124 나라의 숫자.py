# '124' 중에서 n에서 -1 한 숫자의 %3 값을 더해나감

# def solution(n):
#     answer = ""
#     while n > 0:
#         n -= 1 # -1
#         answer = '124'[n%3] + answer # '124'에서 n%3 값을 구하여 answer과 합함, answer 값을 뒤에 더하는 이유는 일의 자리부터 차례대로 구하기 때문
#         n //= 3
        
#     return answer

def solution(n):
    answer = ""
    while n > 0:
        answer = "124"[(n-1) % 3] + answer
        n = (n-1) // 3
    
    return answer
