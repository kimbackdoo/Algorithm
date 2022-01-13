# import datetime

# def solution(a, b):
#     days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
#     return days[datetime.date(2016, a, b).weekday()] # datetime.date, weekday를 이용하여 해당 날짜의 요일 구하기

def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1월 ~ 12월까지 모든 일수를 미리 리스트로 선언
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    return week[(sum(days[:a - 1]) + b) % 7 - 1] # ((a - 1)월까지의 일수 총합 + b) % 7 - 1 하게 되면 현재 날짜의 인덱스가 됨
