# def solution(phone_number):
#     return "*" * (len(phone_number) - 4) + phone_number[-4:] # "*"에 phone_number의 길이 -4 만큼 곱하고 뒤에 4자리 붙임

def solution(phone_number):
    return "*" * len(phone_number[:-4]) + phone_number[-4:] # 뒤에 4자리를 제외하고 *를 붙임
