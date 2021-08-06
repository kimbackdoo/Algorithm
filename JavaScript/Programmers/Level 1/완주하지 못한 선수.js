// splice를 사용하였지만 시간초과
// participant, completion을 각각 오름차순 정렬 후 첫번째 요소부터 모든 요소 비교
// 중간에 요소가 같지 않으면 해당 요소 return, 해당 요소가 제일 끝에 있을 수 있으므로 중간에 return 되지 않으면 마지막 요소 return

// function solution(participant, completion) {
//     participant.sort();
//     completion.sort();
    
//     for (let i = 0; i < completion.length; i++) {
//         if (completion[i] !== participant[i]) {
//             return participant[i]; // 중간에 같지 않은 요소가 있다면 해당 요소 return
//         }
//     }
    
//     return participant[participant.length - 1]; // 중간에 같지 않은 요소가 없다면 즉, 끝 요소를 제외하고 모두 같다면 끝 요소 return
// }

// participant의 각 요소들을 key로 설정, value의 초기값은 1
// 동명이인이 있을 수 있으므로 똑같은 이름 즉, 같은 key가 있을 경우 value 값만 1 증가
// completion의 각 요소들을 순회하면서 해당하는 key 값의 value 값을 1 감소, 즉, 완주한 선수 제외
// value 값이 0이 아니라면 완주하지 못한 선수이므로 해당 요소 return 

function solution(participant, completion) {
    const hash = {}; // participant의 각 요소들을 key로 담을 객체
    // for...in은 객체 순회에 최적화 되어 있으므로 배열은 for...in을 사용하면 성능이 떨어짐
    // 따라서 for...of나 forEach 메소드를 사용해야 함
    for (let p of participant) { // participant의 모든 요소를 순회
        if (!hash[p]) { // p가 hash에 없으면 
            hash[p] = 1; // 초기 value를 1로 설정
            continue;
        }
        
        hash[p]++; // p가 hash에 있으면 value 값 1 증가
    }
    
    completion.forEach(c=> hash[c]--); // completion의 모든 요소를 순회하면서 hash에서 해당하는 value 값 1 감소
    
    for (let key in hash) { // hash는 객체이므로 for...in을 사용하여 모든 key 순회
        if (hash[key]) { // value 값이 0이 아니라면
            return key; // 해당 key return
        }
    }
}
