# 사각형이 정확하게 나뉘는 지점의 개수가 w, h의 최대 공약수
# 따라서 w + h - gcd(w, h)가 사용할 수 없는 사각형의 개수가 된다.

from math import gcd

def solution(w, h):
    return (w * h) - (w + h - gcd(w, h))
