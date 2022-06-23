// 전형적인 DP 알고리즘 문제
// n이 1일때부터 계산해보면, n = 1, 2, 3, 4, 5, ... 일때, 1, 2, 3, 5, 8, ... 형식으로 나감
// 위 규칙을 식으로 도출하면 f(n) = f(n - 1) + f(n - 2) (n >= 2)
function solution(n) {
    const answer = [1, 1]; // answer 배열에 초기값 설정
    // i = 2부터 n + 1까지 순회하면서 위 점화식 적용
    for (let i = 2;  i < n + 1; i++) {
        // n이 커질때, 해당 값도 기하급수적으로 커지므로 계산할때마다 나머지 값만 저장
        answer[i] = (answer[i - 1] + answer[i - 2]) % 1000000007;
    }
    // n번째 요소 return
    return answer[n];
}
