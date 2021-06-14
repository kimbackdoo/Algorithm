# def solution(d, budget):
#     d.sort() # 예산이 제일 적은 부서부터 budget 지원해야 최대로 지원해줄 수 있음
    
#     answer = 0
#     for money in d:
#         if budget >= money: # budget이 각 부서 예산보다 크거나 같다면
#             budget -= money # budget에서 각 부서 예산만큼 빼기
#             answer += 1 # 그때마다 count
    
#     return answer
  
 def solution(d, budget):
    d.sort()
    while budget < sum(d): # budget이 각 부서의 신청 예산의 합보다 작다면
        d.pop() # 제일 큰 값 pop
    
    return len(d) # 남은 d의 길이가 budget을 지원해줄 수 있는 최대값
