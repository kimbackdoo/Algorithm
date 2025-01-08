function solution(genres, plays) {    
    const albums = genres.reduce((result, genre, index) => {
        const { totalPlay = 0, counts = [] } = result[genre] ?? {}
        const currentPlay = plays[index]
        return { ...result, [genre]: { totalPlay: totalPlay + currentPlay, counts: [...counts, [index, currentPlay]] }}
    }, {})
    
    return Object.values(albums)
            .sort((a, b) => b.totalPlay - a.totalPlay)
            .flatMap(({ counts }) => 
                counts.sort((a, b) => {
                    if (a[1] < b[1]) return 1
                    if (a[1] > b[1]) return -1
                    return a[0] - b[0]
                })
                .slice(0, 2))
            .map((item) => item[0])
}