def prime_cnt(n): # 소수 체크
    for i in range(2, int(n**0.5)+1): # 제곱근까지만 반복하여 소수 찾음
        if n % i == 0: # 나누어 떨어지는 수가 있으면 소수가 아니므로
            return False # False 반환
            
    return True

def solution(n):
    answer = 0
    for num in range(2, n+1): # 1 ~ n까지 소수 찾기, 1은 소수가 아니므로 2부터 찾음
        if prime_cnt(num): 
            answer += 1
    
    return answer
