function convertToSecond(time) {
    const [minute, second] = time.split(":").map(Number)
    return minute * 60 + second
}

function formatTime(second) {
    const [min, sec] = [Math.floor(second / 60), second % 60]
    return `${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`
}

function solution(video_len, pos, op_start, op_end, commands) {
    const second = {
        videoLen: convertToSecond(video_len),
        pos: convertToSecond(pos),
        opStart: convertToSecond(op_start),
        opEnd: convertToSecond(op_end),
    }

    const run = {
        skipOpening: () => {
            const isSkipOpening = second.opStart <= second.pos && second.pos <= second.opEnd
            if (!isSkipOpening) return
            second.pos = second.opEnd
        },
        prev: () => second.pos = Math.max(0, second.pos - 10),
        next: () => second.pos = Math.min(second.videoLen, second.pos + 10),
    }
    
    commands.forEach((command) => {
        run.skipOpening()
        run[command]()
        run.skipOpening()
    })
    
    return formatTime(second.pos)
}