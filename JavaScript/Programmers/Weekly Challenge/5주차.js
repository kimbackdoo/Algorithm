// dfs 알고리즘을 이용하여 완전 탐색으로 word의 위치를 찾음

// function solution(word) {
//     function dfs(p) { // dfs 알고리즘 구현
//         if (p.length > 5) return; // p의 길이는 최대 5이므로 5보다 크다면 재귀 탈출
        
//         // answer, cnt는 dfs 함수 안에는 정의되어 있지 않지만 solution 함수에 정의되어 있으므로 스코프 즉, 변수에 접근할 수 있는 범위가 dfs에서 solution으로 확대됨
//         answer[p] = cnt; // 각각의 경우에 대해 위치를 저장
//         cnt++; // cnt 값 1 증가
//         for (let w of "AEIOU") { // A, E, I, O, U에 대해 모든 경우를 찾기 위해 dfs 탐색
//             dfs(p + w);
//         }
//     }
    
//     const answer = {}; // key는 각각의 경우, value는 해당 위치를 저장할 객체
//     let cnt = 0; // 해당 경우의 위치를 찾기위한 변수
//     dfs(""); // dfs 탐색 시작
//     return answer[word]; // answer 객체에서 word에 해당하는 값 return
// }

// dfs, 이분탐색 알고리즘을 적용하여 word의 위치를 찾음

function solution(word) {
    function dfs(p) { // dfs 알고리즘 구현
        if (p.length > 5) return;
        
        answer.push(p);
        for (let w of "AEIOU") {
            dfs(p + w);
        }
    }
    
    function binary_search(start, end) { // 이분탐색 알고리즘 구현
        while (start <= end) {
            let mid = parseInt((start + end) / 2);
            
            if (answer[mid] === word) { // answer[mid]가 word와 같다면 해당 인덱스 return
                return mid;
            } else if (answer[mid] > word) { // answer[mid]가 word보다 크다면 end 값 줄임
                end = mid - 1;
            } else { // answer[mid]가 word보다 작다면 start 값 늘림
                start = mid + 1;
            }
        }
    }
    
    const answer = []; // 모든 경우을 저장할 배열
    dfs(""); // dfs 탐색 시작
    return binary_search(0, answer.length - 1); // 이분탐색을 통해 word의 위치를 찾음
}
