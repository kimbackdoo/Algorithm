# 문자열을 정렬하게 되면 비슷한 i번째와 i+1번째만 일치하는지 확인하면 됨 즉, 이중 for문 사용 안해도 됨
# i+1번째 문자열이 i번째 문자열을 포함하면서 접두어인 경우
# 즉, find 함수를 이용하여 인덱스가 0이면 False를 반환

# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].find(phone_book[i]) == 0:
#             return False
    
#     return True

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]): # zip을 이용하여 묶은 후 반복
        if p2.startswith(p1): # startswith를 이용하여 문자열이 접두어에 포함되는지 아닌지 확인
            return False
    return True
