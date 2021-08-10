// 문제 조건에 따라 구현
// 행과 열을 바꿔서 계산하는 부분이 관건

// function grade(score) { // 학점 계산하는 함수
//     switch(Math.trunc(score / 10)) { // 학점을 계산할 때 10으로 나눈 몫으로 구함
//         case 10:
//         case 9: return "A";
//         case 8: return "B";
//         case 7: return "C";
//         case 6:
//         case 5: return "D";
//         default: return "F";
//     }
// }

// function solution(scores) {
//     const transpose = scores.reduce( // reduce 메소드를 이용하여 행과 열을 바꿔서 return
//         (result, row)=> row.map((_, idx)=> [...(result[idx] || []), row[idx]]) // result[idx] 값이 있다면 result[idx]에 row[idx]를 연결시킴
//                                                                                // result[idx] 값이 없다면 빈 배열에 row[idx]를 연결시킴
//     , []); // 초기값 빈 배열로 설정, reduce 메소드를 사용할 때 항상 초기값 설정해줄 것
//     return transpose.reduce((answer, current, idx)=> { // reduce 메소드를 이용하여 행과 열을 바꾼 배열에서 학점을 도출
//         let len = 0
//         const total = current.reduce((sum, score)=> { // 현재 행의 점수를 구함
//             // 현재 점수가 본인 점수이고, 유일한 최고점 또는 최저점이라면, 이때 filter 메소드를 이용
//             if (score === current[idx] && (score === Math.max(...current) || score === Math.min(...current)) && current.filter(a=> a === score).length === 1) {
//                 return sum; // 본인 점수 더하지 않음
//             }
//             // 조건이 아니라면
//             len++; // 학생 수 count
//             return sum + score; // 현재 점수 더함
//         }, 0);
        
//         return answer + grade(Math.trunc(total / len)); // Math.trunc를 사용하여 평균의 소수점을 잘라내고 학점을 구함 
//     }, "");
// }

// 학점을 계산하는 함수를 따로 만들지 않고, "FFFFFDDCBAA" 문자열을 이용하여 학점을 구함

// function solution(scores) {
//     const transpose = scores.reduce(
//         (result, row)=> row.map((_, idx)=> [...(result[idx] || []), row[idx]])
//     , []);
//     return transpose.reduce((answer, current, idx)=> {
//         let len = 0
//         const total = current.reduce((sum, score)=> {
//             if (score === current[idx] && (score === Math.max(...current) || score === Math.min(...current)) && current.filter(a=> a === score).length === 1) {
//                 return sum;
//             }
            
//             len++;
//             return sum + score;
//         }, 0);
        
//         return answer + "FFFFFDDCBAA"[Math.trunc(total / len / 10)]; // 평균을 10으로 나누고 소수점을 잘라내어 학점을 구함
//     }, "");
// }

// reduce 메소드 대신 map 메소드를 이용하여 매핑

function solution(scores) {
    return scores[0].map((_, c) => scores.map(r => r[c])) // 행과 열을 바꿈, 행에서 열에 해당하는 숫자를 뽑아 배열로 만듦, 2차원 배열이므로 map 메소드도 2개 있어야함
                                                          // scores[0]가 [1, 2, 3, 4, 5]라면 각 요소에 행과 열이 바뀐 배열이 들어옴
                                                          // [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]] 이런식으로 매핑
        .map((s, i) => [...s.splice(i, 1), s]) // 본인 점수를 잘라냄 즉, [1, [2, 3, 4, 5]] 이런식으로 만듦
        .map(([m, s]) => Math.min(...s) <= m && m <= Math.max(...s) ? [m, ...s] : s) // 본인의 점수가 유일한 최고점 또는 최저점이 아니라면 본인 점수와 배열 s를 합침
                                                                                     // 본인의 점수가 유일한 최고점 또는 최저점이라면 s만 return
        .map(s => "FDDCBAA"[Math.max(parseInt(s.reduce((a, c) => a + c) / s.length / 10) - 4, 0)]) // reduce 메소드를 이용하여 평균을 구하고 10으로 나누어 소수점을 잘라냄
                                                                                                   // 문자열의 길이가 10이 아닌 6이므로 나온 값에 -4를 하고, 0과 비교하여
                                                                                                   // 최대값에 해당하는 학점을 구함
        .join(""); // 결과는 배열이므로 join 메소드를 이용하여 문자열로 합침
}
