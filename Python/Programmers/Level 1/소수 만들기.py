from itertools import combinations

def solution(nums):
    nums = list(combinations(nums, 3))
    
    answer = 0
    for num in nums:
        for i in range(2, int(sum(num) ** 0.5) + 1): # for 범위 2 ~ int(sum(num) ** 0.5) 까지!!
            if sum(num) % i == 0:
                break
            elif i == int(sum(num) ** 0.5):
                answer += 1
    
    return answer
