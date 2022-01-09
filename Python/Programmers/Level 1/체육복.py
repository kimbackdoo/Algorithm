# 그리디 : 결과는 찾는 기준에서 항상 최적의 해를 구해야함

# # set은 순서가 정해져 있지 않으므로 예를 들어, 10, [8, 10], [6,7,9] 경우에는 오답
# def solution(n, lost, reserve):
#     # lost, reserve 각각 차집합을 구함 즉, lost, reserve에 겹치는 부분 제거
#     lostSet = set(lost) - set(reserve)
#     reserveSet = set(reserve) - set(lost)
    
#     for r in reserveSet:
#         if r-1 in lostSet: # r-1이 차집합 lostSet에 속한다면
#             lostSet.remove(r-1)
#         elif r+1 in lostSet: # r+1이 차집합 lostSet에 속한다면
#             lostSet.remove(r+1)
    
#     return n - len(lostSet)

# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#     for r in reserve:
#         if r in lost: # r이 lost에 속한다면
#             lost.remove(r)
#         # 본인 체육복을 읽어버리면 본인이 입는다
#         elif r in lost and r-1 not in reserve: # r-1이 lost에 속하면서, r-1이 reserve에 속하지 않는다면
#             lost.remove(r)
#         elif r+1 in lost and r+1 not in reserve: # r+1이 lost에 속하면서, r+1이 reserve에 속하지 않는다면
#             lost.remove(r)
            
#     return n - len(lost)

def solution(n, lost, reserve):
    set_reserve, set_lost = set(reserve) - set(lost), set(lost) - set(reserve)
    
    answer = 0
    for l in set_lost:
        # remove, discard 메소드의 차이는 discard는 해당 원소가 없어도 에러는 발생시키지 않는다. 따라서 discard 메소드가 더 유연함
        # l - 1 이 set_reserve에 속한다면 discard 메소드를 이용하여 해동 원소 제거
        if (l - 1) in set_reserve: set_reserve.discard(l - 1)
        # l + 1 이 set_reserve에 속한다면 discard 메소드를 이용하여 해동 원소 제거
        elif (l + 1) in set_reserve: set_reserve.discard(l + 1)
        # 체육복을 빌릴 수 없으면 count
        else: answer += 1
    
    return n - answer
