# def solution(absolutes, signs):
#     for i in range(len(signs)):
#         if not signs[i]: absolutes[i] *= (-1) # signs[i] 값이 False면 *-1
            
#     return sum(absolutes)

def solution(absolutes, signs):
    # 리스트 컴프리헨션과 sum함수 이용하여 합을 구함
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs)) ])
