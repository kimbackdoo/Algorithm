// 약수의 개수는 1은 1개, 2는 2개, 3은 2개, 4는 3개, 5는 2개, 6은 4개, 7은 2개, 8은 4개, 9는 3개, ...
// 즉, n의 제곱근이 정수이면 약수의 개수는 홀수, 나머지는 짝수가 됨

// function solution(left, right) {
//     let answer = 0;
//     for (let num = left; num <= right; num++) {
//         // Number.isInteger 메소드를 이용하여 제곱근이 정수인지 확인
//         answer += (Number.isInteger(num ** 0.5) ? -num : num); // 제곱근이 정수이면 뺄셈, 정수가 아니면 덧셈
//     }
    
//     return answer;
// }

// answer 배열에 left부터 right까지 모든 숫자를 넣고 reduce 메소드를 이용하여 return

function solution(left, right) {
    let answer = [];
    for (let num = left; num <= right; num++) {
        answer.push(num); // left ~ right까지 모든 숫자 push
    }
    
    return answer.reduce((accumulator, current)=> { // reduce 메소드를 이용하여 값을 구함
        return accumulator + (Number.isInteger(current ** 0.5) ? -current : current); // 제곱근이 정수이면 뺄셈, 정수가 아니면 
    }, 0);
}
