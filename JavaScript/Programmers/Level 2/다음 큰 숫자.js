// n이 1씩 커질때마다 n을 이진수로 바꿨을 때 1의 개수가 같은지 확인

// function solution(n) {
//     // toString(2) 메소드를 이용하여 n을 2진수로 변환 후 나머지 문법을 이용하여 배열로 변환
//     // 이후 filter 메소드를 이용하여 1의 개수를 카운팅
//     const init = [...n.toString(2)].filter((bin) => bin === "1").length;
//     while (true) {
//         // n이 1씩 커질때마다 2진수로 변환 후 1의 개수 카운팅
//         const next = [...(++n).toString(2)].filter((bin) => bin === "1").length;
//         if (init === next) return n; // 1의 개수가 같으면 n return
//     }
// }

// function solution(n) {
//     const init = n.toString(2).match(/1/g).length; // 정규식을 사용하여 1의 개수를 구함, match 메소드는 pattern과 일치하는 항목들을 배열로 변환
//     while (true) {
//         if (init === (++n).toString(2).match(/1/g).length) return n; // 1의 개수가 같으면 n return
//     }
// }

function solution(n) {
    const init = n.toString(2).match(/1/g).length;
    while (init !== (++n).toString(2).match(/1/g).length) {} // while 조건식에 1의 개수 비교하는 조건식을 넣고 body를 비워 반복
    return n; // 1의 개수가 같으면 while문 탈출 후 n return
}
