# def solution(numbers):
#     answer = []
#     for number in numbers:
#         if number % 2 == 0:
#             answer.append(number + 1)
#         else:
#             tmp = bin(number)[2:] 
#             i = 1
#             while True:
#                 chk = bin(number + i)[2:]
#                 if tmp.count('1') <= chk.count('1'):
#                     answer.append(number + i)
#                     break
#                 i += 1

#     return answer

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = list('0' + bin(number)[2:]) # 11, 111, ... 경우를 생각해 011, 0111과 같이 앞에 0을 붙인다. 
        idx = ''.join(bin_number).rfind('0') # 0의 위치를 오른쪽에서부터 찾음
        bin_number[idx] = '1' # idx 번째 비트를 1로 변환

        if number % 2 == 1: # 홀수일 경우 idx+1 번째 비트를 0으로 변환
            bin_number[idx + 1] = '0'
    
        answer.append(int(''.join(bin_number), 2))

    return answer
