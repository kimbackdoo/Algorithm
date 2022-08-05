// 문제 요구에 맞게 구현하면 됨

function distance(a, b) {
    // 키패드 객체, 키패드의 각 번호를 좌표로 생각
    const keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                    4: [1, 0], 5: [1, 1], 6: [1, 2],
                    7: [2, 0], 8: [2, 1], 9: [2, 2],
                    "*": [3, 0], 0: [3, 1], "#": [3, 2]};
    
    // 구조분해할당 문법을 이용하여 a, b의 좌표값을 구함
    const [x1, y1] = keypad[a];
    const [x2, y2] = keypad[b];
    
    return Math.abs(x1 - x2) + Math.abs(y1 - y2); // 두 점 사이의 거리 return
}

function solution(numbers, hand) {
    let left = "*", right = "#"; // 처음에 왼손은 "*", 오른손은 "#" 위치에 있으므로 초기값 설정
    return numbers.reduce((ans, num) => { // reduce 메소드를 이용하여 numbers 배열을 하나의 문자열로 변환
        if ([1, 4, 7].includes(num)) { // num이 1, 4, 7 중 하나라면 왼손
            left  = num;
            return ans + "L";
        } else if ([3, 6, 9].includes(num)) { // num이 3, 6, 9 중 하나라면 오른손
            right = num;
            return ans + "R";
        } else { // num이 2, 5, 8, 0 중 하나라면
            // num과 left, num과 right 사이의 거리 중 가까운 곳 손가락 사용
            if (distance(num, left) < distance(num, right)) { // left가 num과 더 가깝다면 왼손
                left = num;
                return ans + "L";
            } else if (distance(num, left) > distance(num, right)) { // right가 num과 더 가깝다면 오른손
                right = num;
                return ans + "R";
            } else { // 거리가 같다면
                if (hand === "left") { // 왼손잡이면 왼손
                    left = num;
                    return ans + "L";
                } else { // 오른손잡이면 오른손
                    right = num;
                    return ans + "R";
                }
            }
        }
    }, "");
}
