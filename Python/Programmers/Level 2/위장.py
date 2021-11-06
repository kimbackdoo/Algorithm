# 의상 종류별로 겹치게 고르면 안되므로 의상 종류 별로 나누고, 각각의 의상 별로 뽑을 경우, 안뽑을 경우를 선택하여 곱하면 됨(경우의 수)
# 예를 들어, a: [1, 2, 3], b: [2, 3, 4]가 있으면 경우의 수는 4 * 4 - 1이 된다.
# 이유는 a를 보면 1, 2, 3을 각각 뽑을 경우 3 + 모두 안뽑을 경우 1 해서 4가 되고, b도 마찬가지이다.
# 결과에서 -1을 하는 최소 하나의 의상을 입어야 하는데 구한 경우에는 모두 안뽑은 경우도 포함되어 있으므로 모두 안뽑는 경우 1을 빼줘야 한다.

# from collections import defaultdict

# def solution(clothes):
#     cloth = defaultdict(list)
#     for name, kind in clothes: # 의상 별로 옷을 나눔
#         cloth[kind].append(name)
    
#     answer = 1
#     for _, names in cloth.items():
#         answer *= (len(names) + 1) # 모든 경우를 구함
        
#     return answer - 1 # 모두 안뽑는 경우를 빼고 return

from collections import Counter

def solution(clothes):
    counter = Counter([kine for _, kine in clothes]) # Counter 모듈을 이용하여 의상 별로 나누지 말고 clothes에서 의상 종류의 개수를 구함
    
    answer = 1
    for _, value in counter.items():
        answer *= (value + 1) # 모든 경우를 구함
        
    return answer - 1 # 모두 안뽑는 경우를 빼고 return
