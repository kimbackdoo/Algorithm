function solution(players, callings) {
    const ranks = {}
    // reduce로 객체 만들 경우 시간 초과
    // reduce 보다 for, forEach가 빠름
    players.forEach((player, index) => ranks[player] = index)
    
    callings.forEach((name) => {
        const index = ranks[name]
        ;[ranks[players[index - 1]], ranks[players[index]]] = [index, index - 1]
        ;[players[index - 1], players[index]] = [players[index], players[index - 1]]
    })
    
    return players
}