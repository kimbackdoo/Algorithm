// function solution(phone_book) {
//     phone_book.sort()
    
//     for (let i = 0; i < phone_book.length - 1; i++) {
//         if (phone_book[i + 1].startsWith(phone_book[i])) return false
//     }
//     return true
// }

function solution(phone_book) {
    return !phone_book.sort().some((phone, index) => {
        if (index === phone_book.length - 1) return false
        return phone_book[index + 1].startsWith(phone)
    })
}