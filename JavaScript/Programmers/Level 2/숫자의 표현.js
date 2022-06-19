// 1부터 연속된 수의 합이 n이 되는지 확인하면 된다.
// 연속된 수가 되려면 n / 2 값보다 작아야함

// function solution(n) {
//     let answer = 0;
//     for (let i = 1; i < n / 2; i++) { // 1부터 연속된 수의 합이 n이 되는지 확인, 초기 시작 숫자
//         let tmp = 0;
//         for (let j = i; j < n + 1; j++) { // 더해지는 숫자
//             tmp += j; // j의 값을 더해나감
//             if (tmp >= n) { // tmp 값이 n보다 크거나 같으면
//                 (tmp === n) && answer++; // 그 중 tmp 값이 n과 같다면 answer 카운팅
//                 break;
//             }
//         }
//     }
    
//     return answer + 1; // n / 2 연산으로 n을 고려하지 않았기 때문에 answer + 1 값 return
// }

// 중첩 for문 대신 while문 사용, 시간은 비슷함

// function solution(n) {
//     let answer = 0, init = 1, currentNum = 0, sum = 0;
//     while (init < n / 2) { // 초기 시작 값인 init이 n / 2보다 작을 동안 반복
//         sum += (init + currentNum); // sum에 init부터 연속된 숫자의 합을 구함
//         if (sum >= n) { // sum이 n 이상이면
//             (sum === n) && answer++; // 그 중 sum이 n과 같다면 answer 카운팅
//             init++; // init 값 1증가
//             // sum과 currentNum 값 초기화
//             sum = 0;
//             currentNum = 0;
//             continue;
//         }
//         currentNum++; // currentNum 값 1증가
//     }    
    
//     return answer + 1;
// }

// 규칙을 찾아보면 n의 약수 중 홀수의 개수가 정답이 됨
// n의 약수는 n의 제곱근 값을 기준으로 대칭됨

function solution(n) {
    let answer = 0;
    for (let i = 1; i <= (n ** 0.5); i++) { // 1부터 n까지 n번 연산을 수행하지 않고 n의 제곱근까지만 연산 수행
        if (n % i === 0) { // i가 약수라면
            const quotient = +(n / i); // i로 나누었을 때 몫도 약수
            if (quotient % 2 === 1) { // 몫이 홀수라면 카운팅
                answer++;
            }
            // 예를 들어, n이 16이라면 약수는 1, 2, 4, 8, 16이 됨. 이때 4는 제곱근 값이기 때문에 중복 카운팅을 막기 위해 (quotient !== i) 조건 추가
            if ((quotient !== i) && (i % 2 === 1)) { // i도 홀수라면 
                answer++;
            }
        }
    }
    
    return answer;
}
