// 문제에서 요구한대로 구현
// 2차원 배열에서 행과 열을 바꿔 생각하는 부분이 중요함.

// function solution(board, moves) {
//     const basket = []; // 뽑힌 인형을 담을 배열
//     return moves.reduce((answer, move) => { // reduce 메소드를 이용하여 결과값을 도출
//         for (let b of board) { // 2차원 배열의 행만 순회
//             if (basket && basket[basket.length - 1] === b[move - 1]) { // basket이 비어있지 않고, basket의 마지막 요소가 현재 행의 move - 1 열 값과 같다면
//                 basket.pop(); // basket 마지막 요소 pop
//                 b[move - 1] = 0; // 현재 요소 0으로 변환
//                 return answer + 2; // basket의 마지막 요소와 현재 요소 2개가 없어지는 것이므로 answer + 2 return
//             }
            
//             if (b[move - 1]) { // 현재 요소가 0이 아니라면
//                 basket.push(b[move - 1]); // 현재 요소 basket에 push
//                 b[move - 1] = 0; // 현재 요소 0으로 변환
//                 return answer; // 터트려져 사라진 인형이 없으므로 answer return
//             }
//         }
        
//         return answer; // 만약 move 요소의 값이 모두 0이라면 아무일도 일어나지 않으므로 answer return
//     }, 0);
// }

// reduce 메소드를 이용하지 않고 단순 for문 이용, 속도 측면에서 빠름

function solution(board, moves) {
    const basket = [];
    let answer = 0;
    for (let move of moves) { // move 즉, 열 고정
        for (let b of board) { // board의 행 순회
            if (b[move - 1]) { // 현재 요소가 0이 아니라면
                if (basket && basket[basket.length - 1] === b[move - 1]) { // basket이 비어있지 않고, basket의 마지막 요소가 현재 요소와 같다면
                    basket.pop(); // bakset 마지막 요소 pop
                    answer++; // 터트려져 사라진 인형 개수 count
                } else { // 아니라면
                    basket.push(b[move - 1]); // 현재 요소 basket에 push
                }
                
                // 현재 요소가 0이 아니라면 위에 if, else문 중 하나를 반드시 수행
                b[move - 1] = 0; // 조건문을 수행하고 현재 요소를 뽑힌 것이므로 0으로 변환하여 뽑힌 것 처리
                break; // 인형 한개가 뽑히면 더 순회하지 않고 break
            }
        }
    }
    
    return answer * 2; // 터트려져 사라진 인형은 2개를 쌍으로 이루므로 answer * 2 return
}
