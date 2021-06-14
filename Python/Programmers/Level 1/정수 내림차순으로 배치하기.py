def solution(n):
    return int("".join(sorted(str(n), reverse=True))) # n을 문자열로 변환 후 역순 정렬 후 다시 문자열로 변환 후 int로 변환
