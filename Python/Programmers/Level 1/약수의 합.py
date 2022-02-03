# def solution(n):
#     # 리스트 컴프리헨션을 이용하여 약수의 합을 구함
#     return sum([num for num in range(1, n+1) if n % num == 0])

# def solution(n):
#     # 1을 제외하고 n을 2로 나누었을 때 몫이 약수 중 제일 큰 수 이므로
#     # (n // 2) + 1 까지만 약수를 확인하여 성능 개선
#     # 이렇게 되면 n의 약수에서 n이 빠지므로 +n을 
#     return n + sum([i for i in range(1, (n//2)+1) if n%i==0])

def solution(n):
    # for문의 범위를 n의 제곱근까지 반복하는 것으로 성능 개선
    # 이때 4와 같이 제곱수인 경우 나누는 수와 몫이 같을 수 있으므로 예외 처리
    return sum([d + (0 if d == (n // d) else (n // d)) for d in range(1, int(n ** 0.5) + 1) if n % d == 0])
