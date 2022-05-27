// 상대팀 진영에 최대한 빨리 도착하면 된다.
// bfs 알고리즘을 이용하여 현재 지점에서 갈 수 있는 모든 지점을 체크하고 최단거리를 구함
// 현재 지점에서 다음 지점까지의 최단거리는 현재 지점 +1이 됨을 이용

function solution(maps) {
    const move = [[0, 1], [0, -1], [1, 0], [-1, 0]]; // 캐릭터는 상, 하, 좌, 우 움직일 수 있으므로 상, 하, 좌, 우 좌표 미리 설정
    const [n, m] = [maps.length, maps[0].length]; // maps의 행과 열의 길이
    const queue = []; // 탐색할 queue, 자바스크립트에는 queue가 없기 때문에 shift, push 메소드를 이용하여 queue를 흉내냄
    queue.push([0, 0]); // 초기값 queue에 저장
    while (queue.length) { // queue의 길이가 0이 아닐때까지 즉, 모든 지점을 탐색할 때까지 반복
        const [x, y] = queue.shift(); // shift 메소드를 이용하여 queue의 처음 부분을 꺼냄, 구조분해할당 문법을 이용하여 x, y에 꺼낸 값 저장
        for (let i = 0; i < 4; i++) { // 상, 하, 좌, 우 탐색
            const [nx, ny] = [x + move[i][0], y + move[i][1]]; // 구조분해할당 문법을 이용하여 x, y가 갈 수 있는 다음 지점 nx, ny에 저장
            if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] === 1) { // nx, ny과 maps 안에 있고, maps[nx][ny]에 방문하지 않았으면
                maps[nx][ny] = maps[x][y] + 1; // maps[nx][ny] 값 갱신 즉, maps[nx][ny]까지의 최단거리 저장
                queue.push([nx, ny]) // 모든 지점을 탐색해야 하므로 nx, ny 좌표를 queue에 저장
            }
        }
    }
    
    return maps[n-1][m-1] === 1 ? -1 : maps[n-1][m-1];
}
