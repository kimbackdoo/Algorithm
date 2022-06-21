// 문제 조건대로 구현하면 됨
// 동일한 유저를 여러번 신고하면 신고 횟수는 1회로 처리되는 부분을 주의해야함
// function solution(id_list, report, k) {
//     const answer = {}; // 결과값을 담을 객체
//     const badUserCount = {}; // 신고당한 유저를 카운팅할 객체
//     const user = {}; // { [신고당한 유저]: [...신고한 유저들] }로 저장할 객체
//     id_list.forEach((id) => {
//         // 객체들을 초기화 시킴
//         [answer[id], badUserCount[id], user[id]] = [0, 0, []];
//     });
    
//     // 동일한 유저를 여러번 신고해도 신고 횟수는 1회이므로 Set을 이용
//     new Set(report).forEach((info) => {
//         const [userId, badUserId] = info.split(" ");
//         // key는 신고당한 유저, value는 신고한 유저들 형식으로 저장
//         user[badUserId].push(userId);
//         // 신고당한 유저 카운팅
//         badUserCount[badUserId]++;
//     });
    
//     Object.entries(badUserCount).forEach(([id, count]) => {
//         // 신고당한 유저의 횟수가 k 미만이면 return
//         if (count < k) return;
//         // 신고당한 횟수가 k이상이면
//         // 신고한 유저들 카운팅
//         user[id].forEach((id) => answer[id]++);
//     });
    
//     return Object.values(answer);
// }

// Map을 이용한 풀이
function solution(id_list, report, k) {
    // Set을 이용하여 report의 중복을 제거하고, split한 값으로 변형
    const reports = [...new Set(report)].map((info) => info.split(" "));
    const badUserCount = new Map();
    reports.forEach(([_, badUserId]) => {
        // reports를 순회하면서 신고당한 유저 카운팅
        badUserCount.set(badUserId, badUserCount.get(badUserId) + 1 || 1)
    });
    
    const user = new Map();
    reports.forEach(([userId, badUserId]) => {
        // reports를 순회하면서
        const count = badUserCount.get(badUserId);
        // 신고당한 횟수가 k 미만이면 return
        if (count < k) return;
        // 신고 당한 횟수가 k 이상이면 신고한 유저 카운팅
        user.set(userId, user.get(userId) + 1 || 1);
    });
    
    return id_list.map((id) => user.get(id) || 0); // 문제 조건에 맞게 변환 후 return
}
