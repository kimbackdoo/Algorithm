// 1부터 s.length / 2까지 문자열을 압축시킨 후 제일 짧은 길이 반환
// s.length / 2인 이유는 s.length / 2보다 클 경우에는 압축될 수 없으므로 s.length / 2까지만 압축하고 비교
// function solution(s) {
//     let answer = s.length; // 최대값은 s.length이므로 초기값 설정
//     for (let step = 1; step <= s.length / 2; step++) { // s.length / 2까지만 압축하는게 의미 있으므로 s.length / 2까지만 순회
//         const zipped = []; // 압축 결과들을 담은 배열
//         for (let index = 0; index < s.length; index += step) { // 문자열을 압축하기 위해 0부터 step씩 증가하면서 순회
//             const slice = s.slice(index, index + step); // 압축 문자열 저장
//             const last = zipped[zipped.length - 1]; // zipped 배열의 마지막 값 가져옴
//             if (last && last[0] === slice) { // last 값이 있고, last의 압축 문자열이 slice와 같다면
//                 zipped[zipped.length - 1] = [last[0], last[1] + 1]; // 마자막 값에 count 값만 + 1 진행
//                 continue;
//             }
//             zipped.push([slice, 1]); // last 값이 없거나, slice와 같지 않다면 push
//         }
//         // zipped 배열 순회하면서 문자열 압축
//         const result = zipped.map(([slice, count]) => `${count === 1 ? "" : count}${slice}`).join("");
//         // 최소값 저장
//         answer = Math.min(answer, result.length);
//     }
    
//     return answer;
// }

function solution(s) {
    let answer = s.length;
    for (let step = 1; step <= s.length / 2; step++) {
        let result = "", tmp = s.slice(0, step), count = 1; // 배열에 담아서 비교하지 않고 그때그때마다 문자열 압축하고 저장함
        for (let index = step; index < s.length; index += step) {
            const slice = s.slice(index, index + step);
            if (tmp === slice) { // tmp 값과 slice 값이 같으면 카운팅
                count += 1;
                continue;
            }
            // tmp 값과 slice 값이 같지 않으면
            // 문자열 압축
            result += `${count === 1 ? "" : count}${tmp}`;
            // tmp, count 값 초기화
            tmp = slice;
            count = 1;
        }
        // for문을 다 순회하고 마지막 압축된 문자열 result에 저장
        result += `${count === 1 ? "" : count}${tmp}`;
        // 최소값 저장
        answer = Math.min(answer, result.length);
    }
    
    return answer;
}
