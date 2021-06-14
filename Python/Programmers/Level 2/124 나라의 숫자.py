# '124' 중에서 n에서 -1 한 숫자의 %3 값을 더해나감

def solution(n):
    answer = ""
    while n > 0:
        n -= 1 # -1
        answer = '124'[n%3] + answer # '124'에서 n%3 값을 구하여 answer과 합함
        n //= 3
        
    return answer
