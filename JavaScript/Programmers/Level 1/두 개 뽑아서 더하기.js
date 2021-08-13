// numbers에서 2개의 수를 뽑아 만들수 있는 모든 조합을 구함
// 각 조합마다 합을 구하고 정렬

// function combinations(numbers, pick) { // 조합 구현
//     let result = [];
    
//     if (pick === 1) {
//         return numbers.map(number => [number]);
//     }
    
//     numbers.forEach((fixed, idx) => {
//         const new_nums = numbers.slice(idx + 1);
//         const combination = combinations(new_nums, pick - 1);
//         combination.forEach(item => result.push([fixed, ...item]));
//     });
    
//     return result;
// }

// function solution(numbers) {
//     const answer = combinations(numbers, 2).map(item => item[0] + item[1]); // 각각의 조합마다 합을 구함
//     return [...new Set(answer)].sort((a, b) => a - b); // new Set()을 이용하여 중복을 제거하고 전개문법을 이용하여 배열로 만든 후 오름차순 정렬
// }

// 모든 조합을 구하고, 모든 조합 경우에 대해 합을 구해야 하기 때문에
// 2개의 수를 뽑아 더하는 것이므로 중첩 for문을 이용하여 한번에 구하는 것으로 수정

function solution(numbers) {
    const answer = [];
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            answer.push(numbers[i] + numbers[j]); // 2개의 수를 뽑아 합을 push
        }
    }
    
    return [...new Set(answer)].sort((a, b) => a - b); // new Set()을 이용하여 중복을 제거하고 전개문법을 이용하여 배열로 만든 후 오름차순 정렬
}
