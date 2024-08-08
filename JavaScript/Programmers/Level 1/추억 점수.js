// function solution(name, yearning, photo) {
//     const people = Object.fromEntries(name.map((item, index) => [item, yearning[index]]))
    
//     return photo.map((item) => {
//         return item.reduce((answer, name) => answer + (people[name] || 0), 0)
//     })
// }

function solution(name, yearning, photo) {    
    return photo.map((item) => {
        return item.reduce((answer, person) => answer + (yearning[name.indexOf(person)] || 0), 0)
    })
}