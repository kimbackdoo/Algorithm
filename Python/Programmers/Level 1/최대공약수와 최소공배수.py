def gcd(a, b): # 최대공약수 구현, 유클리드 호제법 사용
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
            
    return a

def lcm(a, b): # 최소공배수 구현, 최소공배수는 a, b의 곱을 최대공약수로 나눈 수
    return a * b // gcd(a, b)


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]
