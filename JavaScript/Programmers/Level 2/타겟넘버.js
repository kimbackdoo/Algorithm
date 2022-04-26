// numbers의 숫자를 더하거나 빼서 target이 되는 개수를 세면 됨
// dfs 알고리즘을 적용하여 더하거나 뺄 수 있는 모든 경우를 찾고, target 개수 count

// function solution(numbers, target) {
//     function dfs(result, idx) { // dfs 알고리즘 구현
//         if (idx === numbers.length) { // idx가 numbers의 길이와 같다면
//             if (result === target) { // result가 target이 같다면 answer 1증가, answer는 dfs 함수에는 없지만 solution 함수에는 있으므로 스코프가 확대됨 
//                 answer++;
//             }

//             return;
//         }
        
//         // numbers의 모든 요소를 더하거나 빼면서 dfs 탐색
//         dfs(result + numbers[idx], idx + 1);
//         dfs(result - numbers[idx], idx + 1);
//     }
    
//     let answer = 0;
//     dfs(0, 0);
//     return answer;
// }

// numbers의 모든 요소를 더하거나 빼는 경우를 세면 되므로
// 예를 들어, numbers가 [1, 1, 1, 1, 1]이라면
// [0] -> [1, -1] -> [0, 2, -2, 0] -> [-1, 1, 1, 3, -3, -1, -1, 1] -> ...
// 위와 같이 모든 경우를 확인하고 target인 경우만 필터림하면 됨

// function solution(numbers, target) {
//     let answer = [0]; // 배열의 초기값 0으로 설정
//     numbers.forEach(num => { // forEach 메소드를 이용하여 numbers의 모든 요소 순회
//         answer = answer.reduce((res, cur) => { // reduce 메소드를 이용하여 answer의 모든 요소를 더하거나 뺀 결과 배열을 만듦
//             res.push(cur + num);
//             res.push(cur - num);
//             return res;
//         }, []);
//     });

//     return answer.filter(num => num === target).length; // 만들어진 answer에서 target과 같은 요소만 필터링 후 길이 return
// }

// for of 문 사용

function solution(numbers, target) {
    let answer = [0];
    numbers.forEach(num => {
        const tmp = [];
        for (let a of answer) {
            tmp.push(a + num);
            tmp.push(a - num);
        }
        answer = tmp;
    });
    
    return answer.filter(num => num === target).length;
}
