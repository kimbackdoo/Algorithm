import datetime

def solution(a, b):
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return days[datetime.date(2016, a, b).weekday()] # datetime.date, weekday를 이용하여 해당 날짜의 요일 구하기
