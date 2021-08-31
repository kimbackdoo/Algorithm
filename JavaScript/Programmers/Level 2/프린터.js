// 문제에서 요구한대로 처음 요소를 빼내고 조건에 맞으면 프린트, 아니면 제일 끝으로 보냄
// 큐 자료구조 이용, shift 메소드 이용

// function solution(priorities, location) {
//     const queue = priorities.map((p, i) => [p, i]); // 중요도의 위치를 기억해야 하므로 각각의 중요도와 인덱스를 묶어서 mapping
//     let answer = 0;
//     while (true) {
//         const print = queue.shift(); // queue에서 처음 요소 빼냄
//         const priority = priorities.shift(); // priorities에서 처음 요소 빼냄
//         if (priority >= Math.max(...priorities)) { // 빼낸 요소가 남음 priorities의 최대값보다 크거나 같다면
//             answer++; // answer 값 증가시킴, 즉, 프린트
//             if (print[1] === location) { // 이때, print[1]이 location과 같다면 break
//                 break;
//             }
//         } else { // priorities에 빼낸 요소보다 큰 값이 하나라도 있으면
//             // 빼낸 요소들 제일 뒤로 보냄
//             queue.push(print);
//             priorities.push(priority);
//         }
//     }
    
//     return answer;
// }

// queue와 priorities 모두 이용하는 것이 아닌 some 메소드를 이용하여 빼낸 요소보다 큰 값이 하나라도 있는지 확인
// some 메소드 : 조건을 만족하는 값이 하나라도 존재하면 true, 아니면 false 반환

function solution(priorities, location) {
    const queue = priorities.map((p, i) => [p, i]);
    let answer = 0;
    while (true) {
        const print = queue.shift();
        if (queue.some(q => q[0] > print[0])) { // some 메소드를 이용하여 빼낸 요소보다 큰 값이 하나라도 존재하면
            queue.push(print); // 빼낸 요소 제일 뒤로 보냄
        } else { // 빼낸 요소가 제일 크거나 같다면
            answer++; // 프린트
            if (print[1] === location) break;
        }
    }
    
    return answer;
}
