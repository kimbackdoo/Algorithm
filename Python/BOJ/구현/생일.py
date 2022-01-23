# 문제 조건대로 구현하면 됨
# 나이순으로 정렬하면 됨
# 연도, 월, 일 순으로 오름차순 정렬하고 첫번째 요소가 제일 나이가 많은 사람, 마지막 요소가 나이가 제일 적은 사람이 된다.
import sys
input = sys.stdin.readline

n = int(input())
student = {} # 학생 정보를 저장할 딕셔너리
for _ in range(n):
  name, d, m, y = input().split()
  student[(int(y), int(m), int(d))] = name # key는 (연, 월, 일) 튜플을, value는 이름을 저장

keys = sorted(student) # 연, 월, 일 순으로 오름차순 정렬
print(student[keys[-1]] + "\n" + student[keys[0]]) # 나이가 가장 적은 사람, 많은 사람 출력
