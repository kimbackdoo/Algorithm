// 연속된 숫자를 숫자 한개로 남기면 됨
// 예를 들어, [1, 1, 3, 3, 0, 1, 1]이라면 결과는 [1, 3, 0, 1]이 되어야함
// 빈 배열을 만들고 배열의 마지막 값이 arr의 현재 값이랑 같으면 연속된 숫자이므로 넘기고, 같지 않으면 배열에 push

// function solution(arr) {
//     const answer = []; // 연속된 숫자를 확인할 배열
//     arr.forEach(num => {
//         // answer가 비어있지 않고, answer의 마지막 값이 num이랑 같으면 return
//         // forEach의 매개변수는 콜백 함수이므로 함수는 continue를 사용하지 못하므로 바로 return
//         if (answer && answer[answer.length - 1] === num) {
//             return;
//         }
            
//         answer.push(num); // answer의 마지막 값이 num이랑 같지 않으면 push
//     });
    
//     return answer;
// }

// 연속된 숫자를 하나의 숫자만 남기고 필터링하는 것이므로 filter 메소드를 생각할 수 있음
// 현재 값이 다음 값이랑 같으면 false, 같지 않으면 true를 return 하여 결국 연속된 숫자를 하나의 숫자만 남기고 필터링
// 배열 [1, 2, 3, 4, 5]가 있으면 배열의 인덱스보다 큰 값으로 배열에 접근하려고 하면 오류가 아닌 undefined가 출력됨

function solution(arr) {
    // 현재 값이랑 다음 값이랑 같으면 false, 같지 않으면 true
    // 예를 들어, arr이 [1, 1, 3, 3, 0, 1, 1]이라면 arr[6]과 arr[6 + 1]을 비교할 때는 1과 undefined를 비교하는 것이고 다르므로 true가 반환됨
    // 결국, 마지막 값도 필터링 됨
    return arr.filter((num,idx) => num !== arr[idx+1]);
}
