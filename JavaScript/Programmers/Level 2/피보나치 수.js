// 문제에서 주어진대로 n번째 피보나치 수를 구하면됨
// n의 범위가 크기 때문에 재귀로 풀면 시간 초과
// 다이나믹 프로그래밍 알고리즘 적용
function solution(n) {
    const dp = Array(n + 1).fill(0); // dp 테이블 생성
    [dp[0], dp[1]] = [0, 1]; // 초기값 설정
    for (let i = 2; i <= n; i++) {
        // 2번째 요소부터 점화식대로 적용
        // 이때 숫자가 계속해서 커지기 때문에 연산이 진행될 때마다 나머지 연산 진행
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
    }
    
    return dp[n];
}
