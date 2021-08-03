// 문제에 나온대로 구현

// function solution(price, money, count) {
//     let answer = 0;
//     for (let i = 1; i < count + 1; i++) {
//         answer += (price * i) // for문을 순회하면서 전체 놀이기구 이용 금액을 구함
//     }

//     return Math.max(0, answer - money); // Math.max 함수를 이용하여 최대값 return
// }

// 놀이기구 이용 금액은 price * 1 + price * 2 + price * 3 + ... + price * count
// 즉, price * (1 + 2 + 3 + ... + count)이므로 price * count * (count + 1) / 2

// function solution(price, money, count) {
//     let answer = parseInt(price * count * (count + 1) / 2) - money; // 위 공식 적용, 정수 몫만을 구하기 위해 parseInt 사용
//     return Math.max(0, answer);
// }

// 놀이기구 이용금액은 항상 정수이므로 이유는 count * (count + 1)은 항상 짝수 * 홀수이거나 홀수 * 짝수이므로 항상 정수가 됨
// 즉, parseInt 함수 사용할 필요 없음

function solution(price, money, count) {
    const answer = price * count * (count + 1) / 2 - money;
    return answer > 0 ? answer : 0; // Math.max 함수 대신 삼항연산자를 사용하여 return
}
