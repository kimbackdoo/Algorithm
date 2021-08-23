// 가로의 길이가 n, 세로의 길이가 m인 직사각형 별을 만들면 됨

// process.stdin.setEncoding('utf8');
// process.stdin.on('data', data => {
//     const n = data.split(" ");
//     const a = Number(n[0]), b = Number(n[1]);
    
//     for (let i = 0; i < b; i++) { // 세로의 길이만큼 반복
//         console.log("*".repeat(a)); // repeat 메소드를 이용하여 "*"을 가로의 길이만큼 반복
//     }
// });

process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    
    const star = `${"*".repeat(a)}\n`; // 벡틱(``)을 이용하여 가로의 길이만큼 "*"을 반복하고 문자열 끝에 개행문자("\n")을 붙여줌
    console.log(star.repeat(b)); // 세로의 길이만큼 별 
});
