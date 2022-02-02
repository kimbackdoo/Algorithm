// arr에서 제일 작은 수를 제거하고 return

// function solution(arr) {
//     const min = Math.min(...arr); // 전개문법과 Math.min 메소드를 사용하여 제일 작은 수 찾음
//     // filter 메소드를 이용하여 제일 작은 수보다 큰 수만 필터링
//     // 이때 filter 메소드를 배열의 모든 요소가 min보다 큰지 확인하기 때문에 속도가 비교적 느림  
//     const answer = arr.filter(n => n > min);
//     return !answer.length ? [-1] : answer; // 필터링된 배열의 길이가 0이면 [-1] return, 아니면 answer return
// }

// // arr의 길이가 1인지 확인하여 1이면 [-1] return, 불필요하게 filter 메소드 실행되지 않음

// function solution(arr) {
//     if (arr.length === 1) {
//         return [-1];
//     }
    
//     const min = Math.min(...arr);
//     return arr.filter(n => n > min);
// }

// arr의 모든 요소가 중복되지 않음을 이용
// indexOf 메소드는 인수와 일치하는 첫번째 요소의 인덱스를 반환

// function solution(arr) {
//     if (arr.length === 1) {
//         return [-1];
//     }
//     // splice 메소드를 이용하여 제일 작은 수 제거, 제일 작은 수를 찾을 때 indexOf 메소드를 이용
//     arr.splice(arr.indexOf(Math.min(...arr)), 1);
//     return arr;
// }

function solution(arr) {
    // Math.min과 indexOf 메소드를 이용하여 제일 작은 숫자의 인덱스를 찾고, splice 메소드를 이용하여 제일 작은 수 한개 삭제
    // splice 메소드의 return 값은 삭제된 요소의 배열을 return 하므로 splice 메소드를 호출한 후의 arr을 return 해야함
    arr.splice(arr.indexOf(Math.min(...arr)), 1);
    // !! 연산자를 이용하여 arr.length의 값을 boolean으로 만듦
    // arr.length가 0이면 false, 0이 아니면 true 이용
    return !!arr.length ? arr : [-1];
}
