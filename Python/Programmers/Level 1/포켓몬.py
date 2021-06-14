# def solution(nums):
#     answer = len(list(set(nums))) # set을 이용하여 중복 제거
#     if answer > len(nums) // 2: # nums의 길이 / 2가 answer보다 작으면 nums의 길이 / 2 반환
#         return len(nums) // 2
#     return answer # 그렇지 않으면 answer 반환
    
def solution(nums):
    return min(len(nums)//2, len(set(nums))) # min 함수를 이용하여 작은 값 반환
