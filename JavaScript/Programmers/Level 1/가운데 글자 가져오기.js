// s의 길이가 홀수일 경우 s.slice(글자의 길이 / 2, 글자의 길이 / 2 + 1)가 가운데 글자가 된다.
// s의 길이가 짝수일 경우 s.slice(글자의 길이 / 2, 글자의 길이 / 2 + 2)가 가운데 글자가 된다.
// 즉, 홀수, 짝수일 경우 상관없이 s.slice(Math.floor((글자의 길이 - 1) / 2), Math.ceil((글자의 길이 - 1) / 2) + 1)이 가운데 글자가 된다.

function solution(s) {
    return s.slice(Math.floor((s.length - 1) / 2), Math.ceil((s.length - 1) / 2) + 1);
}
