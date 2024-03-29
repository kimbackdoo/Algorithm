// n의 약수의 합을 구하면 됨
// n이 12라면 약수는 1, 2, 3, 4, 6, 12, n의 제곱근 3.xxx, 따라서 (1, 12), (2, 6), (3, 4)의 합을 구하면 됨
// n이 15라면 약수는 1, 3, 5, 15, n의 제곱근 3.xxx, 따라서 (1, 15), (3, 5)의 합을 구하면 됨
// 즉, n의 약수의 합을 구할 때 1부터 n의 제곱근까지만 약수인지 아닌지 확인하면 됨
// n이 16이라면 약수는 1, 2, 4, 8, 16, n의 제곱근 4, 따라서 (1, 16), (2, 8), (4, 4)의 합에서 제곱근 값 4를 빼주면 됨
// 즉, n이 제곱수라면 약수의 합에서 제곱근 값을 빼주면 됨

// function solution(n) {
//     let i, answer = 0;
//     for (i = 1; i <= n ** 0.5; i++) { // 1부터 n의 제곱근까지 약수 확인
//         if (!(n % i)) { // 약수라면
//             answer += (i + n / i); // 나누는 수와 몫을 더함
//         }
//     }
    
//     return (i - 1 === n / (i - 1)) ? answer - (i - 1) : answer; // n이 제곱수라면 answer에서 제곱근 값을 빼줌, 제곱수가 아니라면 answer return
// }

function solution(n) {
    let answer = 0;
    for (let d = 1; d <= (n ** 0.5); d++) {
        if (n % d === 0) {
            // n이 제곱수 일때 중복을 계산 로직에서 빼줌
            answer += (d + (d === n / d ? 0 : n / d))
            
        }
    }
    
    return answer;
}
