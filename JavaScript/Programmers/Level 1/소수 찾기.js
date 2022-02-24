// 단순히 모든 숫자가 소수인지 아닌지 제곱근까지 확인하게 되면 숫자가 최대 10 ** 6이므로 효율성에서 시간초과
// 에라토스테네스의 체 알고리즘 적용

// function primeNumber(arr, n) { // 에라토스테네스의 체 알고리즘 구현
//     for (let i = 2; i <= n ** 0.5; i++) { // 예를 들어, n이 120이라면 120의 제곱근인 10까지 확인하면 120까지의 모든 숫자를 체로 거를 수 있음
//         if (!arr[i]) { // 해당 숫자에 방문하지 않았으면
//             for (let j = i ** 2; j <= n; j += i) { // j의 초기값이 i ** 2인 이유는 i * k (k < i)인 수들은 이미 걸러졌기 때문에 i * i부터 거르기 시작함
//                 arr[j] = 1; // i의 모든 배수 체로 거름
//             }
//         }
//     }
    
//     return arr;
// }

// function solution(n) {
//     const prime = [];
//     prime.length = (n + 1);
//     prime.fill(0); // 배열을 0으로 채움
    
//     // 체로 거른 배열을 filter 메소드를 이용하여 소수인 숫자만 필터링
//     // 필터링 된 숫자에는 0, 1도 포함되어 있으므로 -2를 해줌
//     return primeNumber(prime, n).filter(check => !check).length - 2;
// }

function prime(n) { // 에라토스테네스의 체 알고리즘 구현, prime 함수 안에서 소수 구하는 로직 다 넣음
    const seive = Array(n + 1).fill(false);
    seive[0] = seive[1] = true;
    for (let i = 2; i <= n ** 0.5 + 1; i++) {
        if (!seive[i]) {
            for (let j = i ** 2; j <= n; j += i) {
                seive[j] = true;
            }
        }
    }
    
    return seive.filter((visited) => !visited).length; // 소수의 개수 return
}

function solution(n) {
    return prime(n);
}
