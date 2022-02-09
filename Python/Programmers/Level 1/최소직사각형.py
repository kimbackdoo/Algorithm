  # 주어진 sizes를 토대로 가장 작은 지갑을 만들면 됨
  # sizes를 순회하면서 첫번째 배열에 가로, 세로 중 큰 값을 저장하고, 두번째 배열에 가로, 세로 중 작은 값을 저장하여
  # 두 배열의 최대값을 곱하면 됨
  def solution(sizes):
    # 1번 배열에 가로, 세로 중 최대값을 저장
    # 2번 배열에 가로, 세로 중 최소값을 저장
    return max([max(size) for size in sizes]) * max([min(size) for size in sizes])
