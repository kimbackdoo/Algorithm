# def solution(absolutes, signs):
#     for i in range(len(signs)):
#         if not signs[i]: absolutes[i] *= (-1) # signs[i] 값이 False면 *-1
            
#     return sum(absolutes)

# def solution(absolutes, signs):
#     # 리스트 컴프리헨션과 sum함수 이용하여 합을 구함
#     return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs)) ])

# # absolutes[i]가 길기 때문에 1, -1을 곱하는 방법을 사용
# def solution(absolutes, signs):
#     return sum([absolutes[i] * (1 if signs[i] else -1) for i in range(len(absolutes))])

# zip 함수 사용
def solution(absolutes, signs):
    return sum([a * (1 if s else -1) for a, s in zip(absolutes, signs)])
