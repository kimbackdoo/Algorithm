// 문제 조건에 따라 구현하면 된다.

// 문제에서 요구하는 메시지로 변환해주는 함수
function getMessage(userNickName, action) {
    const command = { Enter: "들어왔습니다.", Leave: "나갔습니다." };
    return `${userNickName}님이 ${command[action]}`;
}

function solution(record) {
    const answer = []; // 결과값을 담을 배열
    const history = {}; // 닉네임의 history를 담을 객체
    record.forEach((current) => { // record 순회
        // action이 Leave일 경우, userNickName 값이 undefined가 되는 것을 유의
        const [action, userId, userNickName] = current.split(" ");
        // action이 Leave가 아니라면 history 객체에 userId에 해당하는 userNickName값 저장
        if (action !== "Leave") history[userId] = userNickName;
        // action이 Change일 경우, 최종 결과값에 포함될 필요 없으므로
        // action이 Change가 아닐 경우, [userId, action] 값 형태로 push
        action !== "Change" && answer.push([userId, action]);
    });
    
    // map 메소드를 통해 answer 배열의 값을 문제에서 요구하는 형태
    return answer.map(([userId, action]) => getMessage(history[userId], action));
}
