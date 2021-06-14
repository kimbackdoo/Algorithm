def solution(n):
    answer = 0
    while n != 1:
        if answer == 500: # 500번 반복해도 1이 되지 않으면 -1 반환
            return -1
        
        if n % 2 == 0: n //= 2 # 1-1 단계
        else: n = n * 3 + 1 # 1-2 단계
            
        answer += 1 # 한번 작업할 때마다 count
    
    return answer
