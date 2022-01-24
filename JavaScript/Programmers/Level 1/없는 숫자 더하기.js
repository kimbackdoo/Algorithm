// 0 ~ 9 중에 numbers에 없는 숫자를 찾아 더하면 됨
// 0 ~ 9의 합은 45이고 여기서 numbers의 총합을 빼면 없는 숫자들의 합이 됨

function solution(numbers) {
    // 45에서 numbers의 합을 뺌
    return 45 - numbers.reduce((total, number) => total + number, 0);
}
