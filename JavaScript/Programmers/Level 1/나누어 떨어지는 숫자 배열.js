// arr에서 모든 요소를 divisor로 나누었을 때 나누어 떨어지는 것만 필터링 즉, filter 메소드 이용
// 필터링 된 배열의 길이가 1 이상이면 sort, 0이면 [-1] 반환

function solution(arr, divisor) {
    const answer = arr.filter((el) => !(el % divisor)); // divisor로 나누어 떨어지는 요소만 필터링
    return answer.length ? answer.sort((a, b) => a - b) : [-1]; // answer가 빈배열이 아니면 오름차순 정렬, 빈 배열이면 [-1] return
}
