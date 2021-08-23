// 각 직군 별로 점수의 총합을 구하고, 점수가 제일 높은 직군 return

// function solution(table, languages, preference) {
//     const answer = {};
//     for (let t of table) {
//         const [job, ...score] = t.split(" "); // 구조분해할당 문법과 전개문법을 이용하여 split한 배열을 나눔
//         answer[job] = 0; // answer에 직군을 추가하고 초기값 0으로 설정
//         for (let i = 0; i <= languages.length; i++) {
//             const idx = score.indexOf(languages[i]); // 해당 요소에 해당하는 언어를 찾음
//             if (idx !== -1) { // 언어가 score에 있다면
//                 answer[job] += (5 - idx) * preference[i]; // 해당 언어의 점수와 선호도의 곱을 더해나감, 이렇게 하여 각 직군별로 총 점수 구함
//             }
//         }
//     }
    
//     return Object.entries(answer) // Object.entries 메소드를 이용하여 answer 객체를 [key, value] 배열로 변환
//         // sort 메소드를 이용하여 점수를 기준으로 내림차순
//         // 점수가 같다면 localeCompare을 이용하여 직군을 기준으로 오름차순 정렬
//         .sort((a, b) => !(b[1] - a[1]) ? a[0].localeCompare(b[0]) : b[1] - a[1])[0][0]; 
// }

// 매번 languages, preference 배열을 반복하지 않고, 미리 언어에 대한 선호도를 구해놓고 총 점수를 구함

// function solution(table, languages, preference) {
//     const score = {}; // 언어에 대한 점수를 저장할 객체
//     for (let i = 0; i <= languages.length; i++) {
//         score[languages[i]] = preference[i]; // 해당 언어의 점수를 score에 저장
//     }
    
//     const answer = {};
//     for (let t of table) {
//         const [job, ...language] = t.split(" ");
//         answer[job] = 0;
//         for (let i = 0; i < 5; i++) { // 5점 언어부터 1점 언어까지 총 5가지만 있으므로 5번 반복
//             if (language[i] in score) { // 해당 언어가 점수표에 있으면
//                 answer[job] += (5 - i) * score[language[i]]; // 해당 언어의 점수를 더해나감
//             }
//         }
//     }
//     // 점수를 기준으로 내림차순, 점수가 같다면 직군을 기준으로 오름차순 정렬
//     return Object.entries(answer).sort((a, b) => !(b[1] - a[1]) ? a[0].localeCompare(b[0]) : b[1] - a[1])[0][0];
// }

function solution(table, languages, preference) {
    const score = languages.reduce((dic, lang, i) => { // 반복문이 아닌 reduce를 이용하여 score 객체를 만듦
        dic[lang] = preference[i]; // 해당 언어의 선호도를 dic에 저장 후 return
        return dic;
    }, {});
    
    const answer = {};
    for (let t of table) {
        const [job, ...language] = t.split(" ");
        answer[job] = 0;
        for (let i = 0; i < 5; i++) {
            if (language[i] in score) {
                answer[job] += (5 - i) * score[language[i]];
            }
        }
    }
    
    return Object.entries(answer).sort((a, b) => !(b[1] - a[1]) ? a[0].localeCompare(b[0]) : b[1] - a[1])[0][0];
}
