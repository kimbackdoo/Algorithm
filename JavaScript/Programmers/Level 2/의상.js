/**
 * 종류
 * 1개이고, a개 일 때 -> a -> (a + 1) - 1
 * 2개이고, a개, b개 일 때 -> a + b + ab -> (a + 1)(b + 1) - 1
 * 3개이고, a개, b개, c개 일 때 -> a + b + c + ab + ac + bc + abc -> (a - 1)(b - 1)(c - 1) - 1
 */

function solution(clothes) {
    const dict = clothes.reduce((result, [name, type]) => ({ ...result, [type]: [...(result[type] ?? []), name] }), {})
    return Object.values(dict).reduce((result, { length }) => result * (length + 1), 1) - 1
}