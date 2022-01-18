# 0 ~ 9 중에서 numbers에 없는 숫자들의 합을 구하면됨
# def solution(numbers):
#     # 0 ~ 9까지를 set으로 만들고, numbers를 set으로 만든 후 차집합을 구한 이후 sum 함수를 이용하여 합을 구함
#     return sum(set(range(0, 10)) - set(numbers))

# 결국 0 ~ 9까지의 합에서 numbers의 합을 빼면 정답이 됨
def solution(numbers):
    return 45 - sum(numbers)
