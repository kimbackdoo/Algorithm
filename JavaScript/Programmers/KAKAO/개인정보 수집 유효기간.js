const [YEAR, MONTH] = [12, 28]

function getDay(date) {
    const [year, month, day] = date.split(".").map(Number)
    return year * YEAR * MONTH + month * MONTH + day
}

function solution(today, terms, privacies) {
    const targetDay = getDay(today)
    const termsMap = terms.reduce((result, term) => {
        const [type, expireMonth] = term.split(" ")
        return { ...result, [type]: Number(expireMonth) * MONTH }
    }, {})
    
    return privacies.reduce((result, privacy, index) => {
        const [date, type] = privacy.split(" ")
        const isValid = targetDay <= (getDay(date) + termsMap[type] - 1)
        if (isValid) return result
        return [...result, index + 1]
    }, [])
}