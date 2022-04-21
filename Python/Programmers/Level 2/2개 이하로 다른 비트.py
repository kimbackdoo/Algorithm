# 짝수일 경우 2진수 값은 항상 0으로 끝나기 때문에 그 다음 제일 작은 수는 +1한 값이다.
# 홀수일 경우 2진수 값은 항상 1로 끝나기 때문에 그 다음 제일 작은 수는 오른쪽에서부터 0 값을 찾아 0을 1로 1을 0으로 바꾸면 제일 작은 수가 된다.

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0: # 짝수일 경우 제일 작은 수는 +1 한 값
            answer.append(number + 1)
        else: # 홀수일 경우
            binary = bin(number)[2:] # 숫자를 2진수로 변환
            idx = binary.rfind("0") # 오른쪽에서부터 0값을 찾음
            if idx == -1: # 0을 찾지 못했다면
                binary = "0" + binary # 제일 앞에 0을 붙이고
                binary = list(binary) # 리스트 변환 후
                binary[0], binary[1] = "1", "0" # 0을 1로 그 다음 1을 0으로 변환
            else: # 0을 찾았다면
                binary = list(binary) # 바로 리스트 변환 후
                binary[idx], binary[idx + 1] = "1", "0" # 0을 1로 그 다음 1을 0으로 변환
            
            answer.append(int("".join(binary), 2)) # 2진수 값을 10진수로 변환
                    
    return answer

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
