# def solution(n):
#     return (n**0.5 + 1)**2 if n**0.5 == int(n**0.5) else -1 # 정수 x가 n의 제곱근인지를 확인하려면 n**0.5와 int(n**0.5)가 같은지 확인하면 됨

def solution(n):
    return (n**0.5+1)**2 if n**0.5 % 1 ==0 else -1 # n**0.5 % 1로 제곱근이 정수인지 아닌지 판단 가능
