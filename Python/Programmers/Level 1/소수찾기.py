# def prime_cnt(n): # 소수 체크
#     for i in range(2, int(n**0.5)+1): # 제곱근까지만 반복하여 소수 찾음
#         if n % i == 0: # 나누어 떨어지는 수가 있으면 소수가 아니므로
#             return False # False 반환
            
#     return True

# def solution(n):
#     answer = 0
#     for num in range(2, n+1): # 1 ~ n까지 소수 찾기, 1은 소수가 아니므로 2부터 찾음
#         if prime_cnt(num): 
#             answer += 1
    
#     return answer

# 2부터 n + 1까지 매번 소수인지 체크하면서 중복으로 체크하는 경우가 발생
# 에라토스테네스의 체 알고리즘을 이용하여 효율성 개선
def prime(n): # 에라토스테네스의 체 알고리즘 구현
    numbers = [False] * (n + 1)
    numbers[0] = numbers[1] = True
    for i in range(2, int((n + 1) ** 0.5) + 1): # (n + 1)의 제곱근까지만 순회
        if not numbers[i]:
            for j in range(i ** 2, n + 1, i): # 시작점은 i ** 2로 설정하면 불필요한 연산 최소화
                numbers[j] = True
    
    return numbers.count(False)
            

def solution(n):
    return prime(n)
