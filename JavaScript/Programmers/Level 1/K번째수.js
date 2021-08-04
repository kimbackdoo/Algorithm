// 문제에서 요구한대로 구현
// array에서 i번째부터 j번째까지 자르고 정렬한 후 k번째 요소 반환

// function solution(array, commands) {
//     let answer = [];
//     commands.forEach(item=> { // forEach 메소드를 사용하여 commands의 모든 요소 순회
//         let tmp = array.slice(item[0] - 1, item[1]); // slice 메소드를 이용하여 i번째부터 j번째까지 slice
//         tmp.sort((a, b)=> a - b); // sort 메소드를 이용하여 정렬, js에서 sort는 아스키 코드를 기준으로 정렬하므로 sort에 인수로 compare 함수를 넣어주어야 원하는 정렬을 할 수 있음
//         answer.push(tmp[item[2] - 1]); // k번째 요소 answer push
//     });
    
//     return answer;
// }

// function solution(array, commands) {
//     let answer = [];
//     commands.forEach(item=> {
//         const tmp = array
//                     .slice(item[0] - 1, item[1])
//                     .sort((a, b)=> a - b); // tmp 값은 바뀌지 않으므로 const로 선언, array.slice()를 통해 slice한 배열을 반환 한 후 sort를 이용하여 오름차순 정렬
        
//         answer.push(tmp[item[2] - 1]);
//     });
    
//     return answer;
// }

// map 메소드를 이용하여 원하는 형태의 배열을 return

function solution(array, commands) {
    return commands.map(command=> { // map 메소드를 이용하여 commands의 모든 요소를 순회하면서 원하는 형태의 배열을 얻어냄
        const [start, end, find] = command; // command는 3개의 요소를 가지고 있으므로 3개의 요소를 한번에 받아옴, 이 값들은 변하지 않기 때문에 const로 선언
        const tmp = array
                    .filter((item, idx)=> idx >= start - 1 && idx < end) // filter 메소드를 이용하여 i ~ j 범위에 있는 요소만 걸러냄
                    .sort((a, b)=> a - b); // 걸러낸 배열을 오름차순 정렬
        
        return tmp[find - 1]; // map 메소드를 통해 반환된 새로운 배열에 k번째 요소를 return
    });
}
