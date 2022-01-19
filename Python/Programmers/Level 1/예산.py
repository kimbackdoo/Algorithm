# def solution(d, budget):
#     d.sort() # 예산이 제일 적은 부서부터 budget 지원해야 최대로 지원해줄 수 있음
    
#     answer = 0
#     for money in d:
#         if budget >= money: # budget이 각 부서 예산보다 크거나 같다면
#             budget -= money # budget에서 각 부서 예산만큼 빼기
#             answer += 1 # 그때마다 count
    
#     return answer

#  def solution(d, budget):
#     d.sort()
#     while budget < sum(d): # budget이 각 부서의 신청 예산의 합보다 작다면
#         d.pop() # 제일 큰 값 pop
    
#     return len(d) # 남은 d의 길이가 budget을 지원해줄 수 있는 최대값

# 위 드는 while문에서 매 조건을 확인할때마다 sum 함수가 반복적으로 호출되므로 효율성이 떨어짐
def solution(d, budget):
    answer = 0
    for price in sorted(d): # 최대한 많은 부서를 지원해주기 위해 d를 오름차순 정렬 후 모든 요소 순회
        budget -= price # budget에서 price 차감
        if budget < 0: # budget이 0보다 작으면 더이상 지원해줄 수 없으므로 break
            break
        
        answer += 1 # budget이 0이상이면 아직 지원해줄 수 있으므로 count
    
    return answer
